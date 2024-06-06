import numpy as np
import cv2
import torch
import torch.nn as nn
from torchvision import transforms
import timm
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
from PIL import Image
import os
import torch
from faccent.modelzoo import inceptionv1, inceptionv1_decomposed
import os
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torchvision.transforms import Compose,Resize,ToTensor
import torchvision.transforms.functional as TF
import torch.nn as nn
from PIL import Image
from faccent.utils import get_crop_bounds
from faccent.cam import *
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch import Tensor
from typing import Dict, Iterable, Callable
from collections import OrderedDict
import types
from copy import deepcopy
from torch.utils.data import DataLoader
from torchvision.transforms import Compose,Resize,ToTensor
from faccent.utils import default_model_input_range, default_model_input_size, TargetReached, img_to_img_tensor, LargestCenterCrop, image_data
from faccent.transform import range_normalize
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from faccent.cam import gradient_based_receptive_field, find_crop_bounds,plot_recep_field_and_crop_bounds
from faccent.utils import min_max
import pickle
from faccent import param, transform, render, objectives
from faccent.utils import images_to_video, scale_crop_bounds, show, plot_alpha


rl = torch.nn.ReLU(inplace = False)

def get_topk_indices(tensor, k):
    """
    Returns the top k values' indices from a 3D (C x H x W) tensor.
    The result is a k x 3 array where each row represents the indices (C, H, W) for each of the top k values.
    """
    # Flatten the tensor and get the top k values and their indices
    flat_tensor = tensor.reshape(-1)
    topk_values, flat_indices = torch.topk(flat_tensor, k)

    # Convert flat indices to 3D indices (C, H, W)
    c = tensor.shape[0]
    h = tensor.shape[1]
    w = tensor.shape[2]

    indices_c = flat_indices // (h * w)
    indices_h = (flat_indices % (h * w)) // w
    indices_w = (flat_indices % (h * w)) % w

    # Stack the indices to get a k x 3 array
    topk_indices = torch.stack((indices_c, indices_h, indices_w), dim=1)

    return topk_indices


def topk_mask(v, k):
    # Get the top k values and their indices. Note that largest=True by default.
    values, indices = torch.topk(v, k, largest=True)
    
    # Find the minimum value in the top k values, which will serve as our threshold.
    # This includes the k-th largest value itself in the comparison.
    threshold = values.min()
    
    # Create a binary mask: 1 if the element is greater than the threshold, 0 otherwise.
    mask = v > threshold
    
    return mask  # Ensure the mask is in integer format


from faccent.objectives import *
from faccent.cam import find_crop_bounds


@wrap_objective()
def spatial_channel(layer, target_map, batch=None):
    """Optimize for different directions at different locations in space
       target_map: tensor (CxHXW) of layers shape
    """
    @handle_batch(batch)
    def inner(model):
        map_dot = (model(layer)*target_map.to(model(layer).device)).sum(dim=2)
        return -map_dot.mean()
    
    return inner



@wrap_objective()
def spatial_channel_cosim(layer, target_map, cosine_power=1.0, relu_act=False, crop_bounds = None, batch=None):
    """Optimize for different directions at different locations in space with an additional cosine similarity term
       target_map: tensor (CxHXW) of layers shape
       cosine_power: the power to which the cosine similarity is raised
       relu_act: options(None,'pos','neg') do this computation with respect to the positive are negative terms only
    """
    @handle_batch(batch)
    def inner(model,
              target_map = target_map,
              cosine_power = cosine_power,
              relu_act = relu_act,
              crop_bounds=crop_bounds):
        # Get the activation from the model
        activation = model(layer)
        
        # Ensure target_map is on the same device as the model output
        target_map = target_map.to(activation.device)
        
        if crop_bounds is not None:
            activation = activation[:,:,:,crop_bounds[0][0]:crop_bounds[0][1],crop_bounds[1][0]:crop_bounds[1][1]]
            target_map = target_map[:,crop_bounds[0][0]:crop_bounds[0][1],crop_bounds[1][0]:crop_bounds[1][1]]
        
        # Flatten the CxHxW dimensions to compute dot product and cosine similarity
        activation_flat = activation.view(activation.shape[0], activation.shape[1], -1)  # txbx(c*hxw)
        target_map_flat = target_map.flatten()
        
        if relu_act:
            mask = (target_map_flat != 0.).float()
            activation_flat = activation_flat*mask
            
        
        # Compute dot product
        dot_product = (activation_flat * target_map_flat).sum(dim=2)  # Sum over the flattened CxHxW dimensions
        
        # Compute cosine similarity
        activation_norm = activation_flat.norm(dim=2, keepdim=True)  # Norm over the flattened CxHxW dimensions
        target_map_norm = target_map_flat.norm()
        cosine_similarity = (activation_flat * target_map_flat).sum(dim=2) / ((activation_norm * target_map_norm).squeeze())
        
        # Raise cosine similarity to the specified power
        cosine_similarity_powered = cosine_similarity.pow(cosine_power)
        
        # Multiply dot product by cosine similarity (raised to the power)
        objective = -(dot_product * cosine_similarity_powered).mean()  # Average over all dimensions
        
        return objective

    return inner







from faccent.modelzoo import inceptionv1, inceptionv1_decomposed

#model
model_name = 'inception'


DEVICE = 'cuda:0'
device = DEVICE
model = inceptionv1_decomposed(pretrained=True, redirected_ReLU=False)
_ = model.to(DEVICE).eval()
#convert_relu_layers(model) #make relus not 'inplace'
MODEL_INPUT_SIZE = model.model_input_size
MODEL_INPUT_RANGE = model.model_input_range



target_layer = 'mixed3b_pre_relu'
cam_layer = 'mixed3a'

units = range(50)
k = 20


recep_field, target_crop_bounds = gradient_based_receptive_field(model,target_layer,
                                   position='middle',
                                   input_size = MODEL_INPUT_SIZE,
                                   input_range=MODEL_INPUT_RANGE,
                                   device=device,
                                   integrate = True,
                                   init_img = None,
                                   crop_threshold = .2,
                                   square = True,
                                   plot = True)


simple_preprocess = transform.compose([
                                        transform.resize(MODEL_INPUT_SIZE),
                                        transform.range_normalize(MODEL_INPUT_RANGE)   
                                        ])
                                     

for unit in units:

    #cam_dict = torch.load('posneg_from_concepts/%s/kmeans_%s_%s.pt'%(model_name,target_layer,str(kmeans_unit)))
    cam_dict = torch.load('posneg_from_concepts/%s/%s_%s.pt'%(model_name,target_layer,str(unit)))

    pos_cams = cam_dict['pos_cams']
    neg_cams = cam_dict['neg_cams']

    try: target_activations = cam_dict['target_activations'][:,int(cam_dict['unit'])]
    except: target_activations = cam_dict['target_activations']
        
    cam_layers = list(pos_cams.keys())

    target_layer = cam_dict['target_layer']

    try: image_folder = cam_dict['dataset_folder']
    except: 
        cam_dict['dataset_folder'] = '/mnt/data/datasets/imagenet/train100/'
        image_folder = cam_dict['dataset_folder'] 


    inception_mapping = pickle.load(open('/mnt/data/datasets/imagenet/inception_labels_mapping.pkl','rb'))
    with open('/mnt/data/datasets/imagenet/inception_labels.txt', 'r') as f:
        category_targets= f.read().splitlines()


        
    if len(target_activations) == 100000:
        image_folder = '/mnt/data/datasets/imagenet/train100/'
        
    if '/val' in image_folder:
        class_folders = True
    else:
        class_folders = False
        
        

    all_images = os.listdir(image_folder)
    all_images.sort()

    transforms = []
    transforms.append(LargestCenterCrop())
    transforms.append(Resize(MODEL_INPUT_SIZE))
    transforms.append(ToTensor())
    transforms.append(range_normalize(MODEL_INPUT_RANGE))
    preprocess = Compose(transforms)

    batch_size = 40

    #dataloader
    kwargs = {'num_workers': 4, 'pin_memory': True, 'sampler':None} 

    dataloader = DataLoader(image_data(image_folder, 
                                    transform=preprocess,
                                    class_folders=class_folders),
                        batch_size=batch_size,
                        shuffle=False,
                        **kwargs
                        )     



    # Dummy forward pass to get the shape of each layer's output

    layer_shapes = {}
    dummy_input = next(iter(dataloader))[0].to(device)
    with layer_saver(model, [target_layer]+cam_layers) as saver:
        dummy_output = saver(dummy_input)
    
    for layer in [target_layer]+cam_layers:
        layer_shapes[layer] = dummy_output[layer].shape[1:]
        

    if len(layer_shapes[target_layer]) > 2:
        crop_position = (layer_shapes[target_layer][1]//2,layer_shapes[target_layer][2]//2)
        crop_bounds = get_crop_bounds((224,224), (layer_shapes[target_layer][1],layer_shapes[target_layer][2]), crop_position, spread=5)
    else: crop_position = None



    E = pos_cams[cam_layer] + neg_cams[cam_layer]
    E_sum = torch.sum(E,dim=(1,2))

    pos_sums = pos_cams[cam_layer].sum(dim=(1,2))
    neg_sums = neg_cams[cam_layer].sum(dim=(1,2))
    diff_sum = pos_sums-neg_sums


    condition1 = topk_mask(E_sum, 1000)
    condition2 = target_activations < target_activations.mean()+target_activations.std()/4
    condition3 = target_activations > target_activations.mean()-target_activations.std()/4

    combined_condition = condition1 & condition2 & condition3
    #combined_condition = condition3 & condition2
    indices = np.where(combined_condition)[0]
    sorted_values, sorted_indices = torch.sort(E_sum[indices])
    # Step 3: Use the sorted indices to rearrange your original list of indices
    high_energy_mid_act = [indices[i] for i in sorted_indices.numpy()]

    sel_indices = high_energy_mid_act

    position = 'middle'                                                          
    num_workers = 2

    #get batch
    img_indices = sel_indices[:k]
    img_batch = []
    for i in img_indices:
        img_path = image_folder+all_images[i]
        img = preprocess(Image.open(img_path))
        img_batch.append(img)
    img_batch = torch.stack(img_batch)
    img_batch = img_batch.to(device)

    #get attribution vector
    with layer_saver(model, target_layer, detach=False) as target_saver:
        with actgrad_extractor(model, cam_layers, concat=False) as score_saver:

            model.requires_grad_(True)
            model.zero_grad()

            batch_target_activations = target_saver(img_batch)[target_layer]
            if position == 'middle':
                batch_target_activations = batch_target_activations[:,:,batch_target_activations.shape[2]//2,batch_target_activations.shape[3]//2]
            elif position is not None:
                batch_target_activations = batch_target_activations[:,:,position[0],position[1]]

            batch_unit_act = batch_target_activations[:,unit]

            #feature collapse
            #loss = loss_f(target_activations)
            #loss = torch.sum(cosim)
            loss = torch.sum(batch_unit_act)
            #overall_loss+=loss
            loss.backward()

            activations = score_saver.activations
            gradients = score_saver.gradients


    actgrads = activations[cam_layer]*gradients[cam_layer]
    act_crop_bounds = find_crop_bounds(torch.abs(actgrads).sum(dim=(0,1)),0.)


    out_thresholds = range(0,81,4)
    trans_p = 2
    optimizer = lambda params: torch.optim.Adam(params, lr=.02)


    img_size = (224,224)
    canvas_size = (512,512)
    crop_buffer=40
    relu_act = False
    cosine_power = 1.0

    scaled_target_crop_bounds = scale_crop_bounds(target_crop_bounds,224,512)
    scaled_buffered_target_crop_bounds = torch.tensor(scaled_target_crop_bounds)
    scaled_buffered_target_crop_bounds[:,0] -= crop_buffer
    scaled_buffered_target_crop_bounds[:,1] += crop_buffer


    #for img_i in green_sel_indices:
    for i in range(10):
        
        img_i = sel_indices[i] 
        
        out_folder = 'accentuations/%s/%s/unit%s_img%s/'%(model_name,target_layer,str(unit),str(img_i))
        os.makedirs(out_folder,exist_ok=True)
        
        img_path = image_folder+all_images[img_i]
        #show crop
        img = img_to_img_tensor(img_path,size = img_size)
        if len(layer_shapes[target_layer]) > 2: 
            img = img[:,:,target_crop_bounds[0][0]:target_crop_bounds[0][1],target_crop_bounds[1][0]:target_crop_bounds[1][1]]
        img = F.interpolate(img, size=img_size)
        print(img_i)

        show(img, normalize = False)

        accent_acts = {'+':[],
                    '-':[]}
        for sign in ['+','-']:
        #for sign in ['-']:

            #obj = spatial_channel(cam_layer,actgrads[i])
            obj1 = spatial_channel_cosim(cam_layer,
                                        rl(actgrads[i]),
                                        relu_act=relu_act,
                                        crop_bounds = act_crop_bounds)
            if sign == '-': obj1 = spatial_channel_cosim(cam_layer,
                                                        rl(-actgrads[i]),
                                                        relu_act=relu_act,
                                                        cosine_power = cosine_power,
                                                        crop_bounds = act_crop_bounds)
    #         obj2 = objectives.l2_compare(reg_layer)
    #         obj = obj1 - reg_alpha*obj2
            obj = obj1

            parameterizer = param.fourier_phase(init_img = img_path,
                                                device=device,
                                                img_size = canvas_size,
                                                forward_init_img = True
                                                )

            transforms = [transform.box_crop(box_min_size=0.9,
                                                box_max_size=0.99,
                                                box_loc_std=0.05,
                                ),
                        transform.uniform_gaussian_noise()
                            ]
            
            #transforms = transform.standard_jitter_transforms


            imgs, img_trs, _, _ = render.render_vis(model,
                                                    obj,
                                                    parameterizer = parameterizer,
                                                    transforms = transforms,
                                                    optimizer = optimizer,
                                                    #img_tr_obj = obj1,
                                                    img_size = canvas_size,
                                                    out_thresholds = out_thresholds,
                                                    inline_thresholds = [],
                                                    trans_p= trans_p)
            
            
            processed_imgs = simple_preprocess(torch.stack(imgs)[:,0]).to(device)
            with layer_saver(model, target_layer, detach=True) as target_saver:
                layer_acts = target_saver(processed_imgs)
            unit_acts = layer_acts[target_layer][:,unit]
            unit_acts = unit_acts[:,unit_acts.shape[1]//2,unit_acts.shape[2]//2]
            
            
            accent_acts[sign] = (unit_acts.detach().cpu()-target_activations.mean())/target_activations.std()
            
            for j in range(len(imgs)):
                plot_alpha(
                imgs[j][0],img_trs[j][0],
                p=trans_p,
                crop=scaled_buffered_target_crop_bounds,
                show=False,
                save = out_folder+'accent%s%s.jpg'%(sign,str(j))
                        )
            
        metadata = {
                    'target_acts':accent_acts,
                    'unit':unit,
                    'cam_layer':cam_layer,
                    'target_layer':target_layer,
                    'position':position,
                    'cosine_power':cosine_power,
                    'trans_p':trans_p,
                    'n_steps':out_thresholds[-1]
        }
                        
        torch.save(metadata, out_folder+'metadata.pt')
        
            
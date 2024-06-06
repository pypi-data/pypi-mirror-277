
import os
from subprocess import call
import torch
from faccent import cam
from faccent.utils import plot_alpha
from torchvision.transforms import CenterCrop, Compose
from captum.attr import NoiseTunnel,Saliency,LayerGradCam, LayerAttribution
import torch.nn.functional as F
from PIL import Image

device = 'cuda:1'
layer = 'mixed4a'
reg_layer = 'conv2d0'
cam_layer = 'mixed3b'
outdir = '/mnt/qnap_data/chris_projects/faccent/human_experiment/mixed4a/'
featureviz_folder = '/mnt/data/chris/dropbox/Research-Hamblin/Projects/faccent/analyses/human_experiment/feature_visualizations/inception'

dataset_activations = torch.load('../metadata/imagenetval_activations.pt')
img_paths = torch.load('../metadata/imagenetval_img_paths.pt')
labels = torch.load('../metadata/imagenetval_labels.pt')
cam_ranges = torch.load('/mnt/data/chris/dropbox/Research-Hamblin/Projects/faccent/analyses/human_experiment/metadata/inception_logit_cam_ranges.pt')


from faccent.modelzoo import inceptionv1
model = inceptionv1(pretrained=True)   #model to run images through
model.to(device)


MODEL_INPUT_SIZE = model.model_input_size    #input size model accepts
MODEL_INPUT_RANGE = model.model_input_range  #range of values model expects

from faccent.transform import resize, range_normalize, compose
from faccent.utils import img_to_img_tensor

transforms = [resize(MODEL_INPUT_SIZE),range_normalize(MODEL_INPUT_RANGE)]
transform_f = Compose(transforms)


from PIL import Image
from faccent.utils import *

ccrop = CenterCrop(224)

def save_tensor_as_image(tensor, filename):
    # Check if the tensor has channels as the first dimension
    # If it does, rearrange to (Height x Width x Channels)
    if tensor.shape[0] == 1 or tensor.shape[0] == 3:
        tensor = tensor.permute(1, 2, 0)
    # Convert tensor values to the range [0, 255]
    tensor = (tensor * 255).byte()
    # Convert the tensor to a PIL Image
    pil_img = Image.fromarray(tensor.numpy())
    # Save the image
    pil_img.save(filename)

import pandas as pd
df = pd.read_csv('superset_metadata.csv')

for trial_id,row in df.iterrows():
    print('trial '+str(trial_id))
    # if trial_id in trial_exclusions:
    #     print('excluding')
    #     continue
    trial_dir = outdir+'experiment_images/'+str(trial_id)+'/'
    # if not os.path.exists(trial_dir):
    #     os.makedirs(trial_dir,exist_ok=True)

    unit = row.unit
    img_idx = row.target_img_idx
    # #match
    # img = img_to_img_tensor(row.match_img_path,size=(224,224)).squeeze()
    # save_tensor_as_image(img, trial_dir+'/match.png')
    # #foil
    # img = img_to_img_tensor(row.distractor_img_path,size=(224,224)).squeeze()
    # save_tensor_as_image(img, trial_dir+'/foil.png')
    # #target
    # img = img_to_img_tensor(row.target_img_path,size=(224,224)).squeeze()
    # save_tensor_as_image(img, trial_dir+'/target.png')


    # #feature viz explaination
    # img = ccrop(img_to_img_tensor('%s/%s.png'%(featureviz_folder,str(unit)))).squeeze()
    # save_tensor_as_image(img, trial_dir+'/explanation_featvizphase.png')
    # #call('cp %s/%s.png %s/explanation_featvizphase.png'%(featureviz_folder,str(unit),trial_dir),shell=True)

    # #max image explaination
    # max_img_idx = int(dataset_activations[:,unit].argmax())
    # img = img_to_img_tensor(img_paths[max_img_idx],size=(224,224)).squeeze()
    # save_tensor_as_image(img,  trial_dir+'/explanation_datasetexample.png')


    img_t = transform_f(img_to_img_tensor(row.target_img_path,crop=True)).to(device).requires_grad_(True)
    np_image = np.array(Image.open(row.target_img_path).resize((224,224)))/255.
    #cam explaination
    explainer = LayerGradCam(model,model.mixed5b)
    attribution = explainer.attribute(img_t, target=unit,relu_attributions=True).detach().cpu()
    attribution = F.interpolate(attribution, size=(224, 224), mode='bilinear', align_corners=True).squeeze()
    attribution = attribution.repeat(3,1,1)
    plt.clf()
    plot_attribution(np.transpose(attribution.numpy(),(1,2,0)),
                              np_image,
                              absolute_value=True,
                              alpha=.4,
                              clip_percentile = .1,
                              save = trial_dir+'/explanation_gradcam.png'
                )
    #smoothgrad explaination
    explainer = Saliency(model)
    nt = NoiseTunnel(explainer)
    attribution = nt.attribute(img_t, nt_type='smoothgrad',stdevs=30.,
                            nt_samples=40, target=unit).cpu().squeeze()
    plt.clf()
    plot_attribution(np.transpose(attribution.numpy(),(1,2,0)),
                              np_image,
                              absolute_value=True,
                              alpha=.4,
                              clip_percentile = .1,
                              save = trial_dir+'/explanation_smoothgrad.png'
                )


    # #accent
    # if not os.path.exists(outdir+'accent_data/'+str(trial_id)+'.pt'):
    #     call_str = ('python gen_accent.py '
    #                 '--unit {unit} '
    #                 '--layer "{layer}" '
    #                 '--reg-layer "{reg_layer}" '
    #                 '--img-path "{img_path}" '
    #                 '--out-path "{out_path}" '
    #                 '--device "{device}"').format(
    #                 unit=unit,
    #                 layer=layer,
    #                 reg_layer=reg_layer,
    #                 img_path=row.target_img_path,
    #                 out_path=outdir+'accent_data/'+str(trial_id)+'.pt',
    #                 device=device
    #             )
    #     call(call_str,shell=True)

    # accent_d = torch.load(outdir+'accent_data/'+str(trial_id)+'.pt')
    # pos_cams, neg_cams, _ = cam.cam_maps_from_dataloader(row.target_img_path,
    #                                                 model,
    #                                                 layer,
    #                                                 unit,
    #                                                 [cam_layer],
    #                                                 model_input_range=MODEL_INPUT_RANGE
    #                                                 )

    # range_min,range_max = cam_ranges[unit][0][0], cam_ranges[unit][0][1]
    # threshold_pos_map = cam.thresholded_linear_map(pos_cams[cam_layer],range_min,range_max)
    # upsampled_threshold_pos_map = cam.bilinear_upsample(threshold_pos_map.squeeze(), (512,512))
    # expanded_upsampled_threshold_pos_map = torch.tensor(upsampled_threshold_pos_map).unsqueeze(0).unsqueeze(0).repeat(1, 3, 1, 1)
    # combined_trs = expanded_upsampled_threshold_pos_map*accent_d['img_trs'][-1]
    # img = F.interpolate(accent_d['imgs'][-1], size=(224, 224), mode='bilinear', align_corners=True)
    # tr = F.interpolate(combined_trs, size=(224, 224), mode='bilinear', align_corners=True)

    # plt.clf()
    # plot_alpha(img,tr,
    #        show=False,
    #        save = trial_dir+'/explanation_accent_fullmask.png')
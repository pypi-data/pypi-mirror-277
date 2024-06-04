#!/usr/bin/env python
# coding: utf-8

# In[1]:


from imutils import paths
import os
import cv2
from tqdm import tqdm
import shutil
import pandas as pd
from anomalib.models import Patchcore
from anomalib.models import get_model
import torch

from anomalib.data.utils import InputNormalizationMethod, get_transforms
from torch.utils.data import DataLoader
from anomalib.data.inference import InferenceDataset
from anomalib.data.utils import get_image_filenames

from anomalib.data import Folder
from anomalib.config import get_configurable_parameters
from anomalib.utils.callbacks import LoadModelCallback, get_callbacks
from pytorch_lightning import Trainer

import urllib.request
from pathlib import Path

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)
        
        
urlModel = "https://www.dropbox.com/scl/fi/nl8xkcvug4hx8k6vju66n/config-patchcore-resnet50.pth?rlkey=6utyudmzkvi0lidg03edtm50p&st=v3gph6py&dl=1"
urlConfig = "https://www.dropbox.com/scl/fi/vycrt7ig6oft3t3zdvjo2/config-patchcore-resnet50.yaml?rlkey=o92c13iu26c49n694jgyrwlrm&e=1&st=22tpm13i&dl=1"

urlModelPath = str(Path.home())+f"{os.sep}.anomalydetection{os.sep}"+ "config-patchcore-resnet50.pth"
urlConfigPath = str(Path.home())+f"{os.sep}.anomalydetection{os.sep}"+ "config-patchcore-resnet50.yaml"





m = "config-patchcore-resnet50.yaml"

def rreplace(s, old, new):
	return (s[::-1].replace(old[::-1],new[::-1], 1))[::-1]


def predict(p):

	if  not os.path.exists(urlModelPath):
		with DownloadProgressBar(unit="B", unit_scale=True,
		                         miniters=1) as t:
		    os.makedirs(os.path.dirname(urlModelPath), exist_ok=True)
		    urllib.request.urlretrieve(urlModel, filename=urlModelPath, reporthook=t.update_to)
		    urllib.request.urlretrieve(urlConfig, filename=urlConfigPath, reporthook=t.update_to)
	shutil.rmtree(p+'/temp',ignore_errors=True)
	os.makedirs(p+'/temp',exist_ok=True)



	print("[Splitting the images]")

	images = list(paths.list_images(p))

	for imPath in tqdm(images):
	    image = cv2.imread(imPath)
	    height, width, _ = image.shape

	    # Calculate the dimensions for the four parts
	    half_width = width // 2
	    half_height = height // 2

	    # Split the image into 4 parts
	    top_left = image[0:half_height, 0:half_width]
	    top_right = image[0:half_height, half_width:width]
	    bottom_left = image[half_height:height, 0:half_width]
	    bottom_right = image[half_height:height, half_width:width]
	    
	    cv2.imwrite(rreplace(imPath[:-4]+"_1.tif",'/','/temp/'),top_left)
	    cv2.imwrite(rreplace(imPath[:-4]+"_2.tif",'/','/temp/'),top_right)
	    cv2.imwrite(rreplace(imPath[:-4]+"_3.tif",'/','/temp/'),bottom_left)
	    cv2.imwrite(rreplace(imPath[:-4]+"_4.tif",'/','/temp/'),bottom_right)
	    # os.remove(imPath)
	    
	images = list(paths.list_images(p+'/temp/'))

	for imPath in tqdm(images):
	    image = cv2.imread(imPath)
	    height, width, _ = image.shape

	    # Calculate the dimensions for the four parts
	    half_width = width // 2
	    half_height = height // 2

	    # Split the image into 4 parts
	    top_left = image[0:half_height, 0:half_width]
	    top_right = image[0:half_height, half_width:width]
	    bottom_left = image[half_height:height, 0:half_width]
	    bottom_right = image[half_height:height, half_width:width]
	    
	    cv2.imwrite(imPath[:-4]+"_1.tif",top_left)
	    cv2.imwrite(imPath[:-4]+"_2.tif",top_right)
	    cv2.imwrite(imPath[:-4]+"_3.tif",bottom_left)
	    cv2.imwrite(imPath[:-4]+"_4.tif",bottom_right)
	    os.remove(imPath)



	# In[2]:



	config = get_configurable_parameters(config_path=urlConfigPath)
	# config.optimization.export_mode = "openvino"


	# In[8]:


	


	# Create the model and engine
	model = torch.load(urlModelPath,map_location=torch.device('cpu'))
	model.eval()
	trainer = Trainer(**config.trainer)


	# In[ ]:




	# In[ ]:



	imagefolder = p+'/temp/' 

	normalization = InputNormalizationMethod('imagenet')

	image_size = 128

	transform = get_transforms(
	    config=None, image_size=image_size, center_crop=None, normalization=normalization
	)

	dataset = InferenceDataset(
		imagefolder, image_size=image_size, transform=transform  # type: ignore
	    )
	dataloader = DataLoader(dataset)

	preds = trainer.predict(model=model, dataloaders=[dataloader])


	# In[ ]:



	predScore = [x['pred_scores'] for x in preds]
	predLabels = [x['pred_labels'] for x in preds]


	# In[ ]:

	
	names = get_image_filenames(p+'/temp/')




	# In[ ]:


	
	df = pd.DataFrame(list(zip(names,predScore,predLabels)),columns=['name','score','label'])


	# In[ ]:


	df['parent'] = df['name'].apply(lambda x: str(x)[:-10])

	df.to_csv(p+'/result.csv',index=None)



	images = list(paths.list_images(p+'/temp/'))

	for imPath in tqdm(images):
	    image = cv2.imread(imPath)
	    os.remove(imPath)
	    
	os.rmdir(p+'/temp/')

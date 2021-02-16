# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:34:11 2021

@author: HP
"""

import os
import cv2
import pickle
import numpy as np

data_dir = os.path.join(os.getcwd(),"pickle_data")
img_dir = os.path.join(os.getcwd(),"images")

def preprossing(image):
    image = cv2.resize(image,(100,100))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return image
images = []
labels = []

                              
for i in os.listdir(img_dir):
    image=cv2.imread(os.path.join(img_dir,i))
    image=preprossing(image)
    images.append(images)
    labels.append(i.split("_")[0])

images=np.array(images)
labels=np.array(labels)

with open(os.path.join(data_dir,"images.p"),"wb")as f:
    pickle.dump(images,f)
with open(os.path.join(data_dir,"labels.p"),"wb")as f:
    pickle.dump(images,f)
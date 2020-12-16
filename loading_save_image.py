# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 01:23:55 2020

@author: Madhur Gupta
"""
from __future__ import print_function
import cv2

import argparse

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='path to image')
args=vars(ap.parse_args())

image=cv2.imread(args['image'])    
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))
cv2.imwrite('MG_dup.jpg',image)
cv2.imshow("Image", image)

cv2.waitKey(0)


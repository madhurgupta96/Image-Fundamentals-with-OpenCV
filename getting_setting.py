# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:52:04 2020

@author: Madhur Gupta
"""
from __future__ import print_function
import cv2

import argparse

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='path to image')
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
cv2.imshow("Original", image)

#setting 0,0 as red pixel
(b,g,r)=image[0,0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g, b))

#setting the corner of image as green

corner=image[0:100,0:100]
cv2.imshow('corner',corner)

image[0:100,0:100]=(0,255,0)
cv2.imshow('Updated',image)
cv2.waitKey(0)
    

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:41:38 2020

@author: Madhur Gupta
"""

import numpy as np
import cv2
# We create a blank space to be used for drawing 

canvas=np.zeros((300,300,3),dtype='uint8')
# lets draw a yellow  line

yellow=(0,255,255)
cv2.line(canvas,(0,0),(300,300),yellow)
cv2.imshow('canvas',canvas)
#cv2.waitKey(0)
# we will draw red line with some thickness
red=(0,0,255)
cv2.line(canvas,(0,300),(300,0),red,3)
cv2.imshow('canvas',canvas)
#cv2.waitKey(0)

# A green recanganle
green=(0,255,0)
cv2.rectangle(canvas,(10,10),(60,60),green,3)
cv2.imshow('canvas',canvas)

cv2.waitKey(0)
# -*- coding: utf-8 -*-
"""
OpenCV 3 学习示例

卷积特性试验

Created on Fri Jul 21 12:49:40 2017

@author: yf
"""

import cv2
import time

#help(cv2.namedWindow)
import numpy as np

from skimage import io
from scipy import ndimage

kernel_3x3 = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

kernel_3x3 = np.array([[0, -0.25, 0],
                       [-0.25,  1, -0.25],
                       [0, -0.25, 0]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])


fileStr = "C:\\Users\\yj_7u\\Pictures\\Icon.bmp"
#fileStr = "C:\\Users\\yj_7u\\Pictures\\p2303767259.jpg"

#fileStr = "C:\\Users\\006\\Pictures\\tx.jpg"
#fileStr = "C:\\Users\\006\\Pictures\\half.jpg"
#fileStr = "E:\\Pics\\Mask.jpg"

image = cv2.imread(fileStr)
imageGrey = cv2.imread(fileStr, 0)


imageB = image[:,:,0]
imageG = image[:,:,1]
imageR = image[:,:,2]

k3B = ndimage.convolve(imageB, kernel_3x3)
k3G = ndimage.convolve(imageG, kernel_3x3)
k3R = ndimage.convolve(imageR, kernel_3x3)



k3 = ndimage.convolve(imageGrey, kernel_3x3)
k5 = ndimage.convolve(imageGrey, kernel_5x5)

blurred = cv2.GaussianBlur(image, (11, 11), 0)
bluredImg = image - blurred


cv2.waitKey(-1)

cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("bluredImg", bluredImg)

#image[:,:,0] = k3B
#image[:,:,1] = k3G
#image[:,:,2] = k3R

cv2.imshow("image", image)

cv2.imshow("3x3B", k3B)
cv2.imshow("3x3G", k3G)
cv2.imshow("3x3R", k3R)

cv2.waitKey(-1)

#cv2.destroyWindow()
cv2.destroyAllWindows()
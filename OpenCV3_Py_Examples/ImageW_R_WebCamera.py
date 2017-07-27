# -*- coding: utf-8 -*-
"""
OpenCV 3 学习示例

基本的图像结构、读取写入的方法
以及使用Camera视频捕捉的功能

Created on Mon Jul 10 15:58:39 2017

@author: yf
"""

import cv2
import time
#help(cv2.namedWindow)
import numpy as np


from skimage import io
from scipy import ndimage

import sys
sys.path.append("..")
import FrameRunner

def testProcess():
    kernel_3x3 = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])
    
    kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                           [-1,  1,  2,  1, -1],
                           [-1,  2,  4,  2, -1],
                           [-1,  1,  2,  1, -1],
                           [-1, -1, -1, -1, -1]])


    #fileStr = "C:\\Users\\yj_7u\\Pictures\\Icon.bmp"
    #fileStr = "C:\\Users\\yj_7u\\Pictures\\p2303767259.jpg"
    
    fileStr = "C:\\Users\\006\\Pictures\\tx.jpg"
    #fileStr = "C:\\Users\\006\\Pictures\\half.jpg"
    image = cv2.imread(fileStr, 0)

    k3 = ndimage.convolve(image, kernel_3x3)
    k5 = ndimage.convolve(image, kernel_5x5)

    blurred = cv2.GaussianBlur(image, (11,11), 0)
    bluredImg = image - blurred

    #cv2.imshow("3x3", k3)
    #cv2.imshow("5x5", k5)
    cv2.imshow("bluredImg", bluredImg)
    if cv2.waitKey(10)>150:
        runner.Stop()
    
#print(image.shape)
#print(image.size)
#print(image.dtype)

#cv2.waitKey(-1)


#----------------------------
# Switch Blue Channel between Red Channel test,OpenCV Reversed
#testImage = image.copy()
#testImage[:,:,2] ^= testImage[:,:,0]
#testImage[:,:,0] ^= testImage[:,:,2] 
#testImage[:,:,2] ^= testImage[:,:,0]

#print(image[0])
#print("----------------------------------------------")
#print(testImage[0])
#---------------------------

#io.imshow(testImage)




#clked = False

def onMouse(evt, x, y, flags, param):
    global runner
    if evt == cv2.EVENT_LBUTTONDBLCLK:
        runner.Stop()
        cv2.destroyAllWindows()
#        
#camCap = cv2.VideoCapture(0)
#
#cv2.namedWindow('VideoWin')



#
#suc, frame = camCap.read()
#
#cv2.imshow('VideoWin', frame)
#cv2.waitKey()

##and cv2.waitKey(1)==-1 
#while suc and not clked:
#    cv2.imshow('VideoWin', frame)
#    suc, frame = camCap.read()
#    cv2.waitKey()
#
#cv2.imshow('VideoWin', frame)
#cv2.waitKey()

#cv2.imshow("TestImg", image)
#cv2.waitKey()
#cv2.imshow("TestImg", testImage)
#cv2.waitKey()

cv2.setMouseCallback('bluredImg', onMouse)
runner = FrameRunner.Runner(1)
runner.Run(testProcess)

#camCap.release()
# -*- coding: utf-8 -*-
"""
SimpleRenderer 简单渲染器

可以设置帧率的渲染器
用于计算机视觉的图像测试
以及使用Camera视频捕捉的功能

Created on Thu Jul 27 13:15:25 2017

@author: yf
"""

import cv2
#import time
import numpy as np
#import math
import FrameRunner
from scipy import ndimage
        
        
class SimpleRenderer(FrameRunner.Runner):
    
    kernel_3x3 = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])

#    kernel_3x3 = np.array([[0, -0.25, 0],
#                           [-0.25,  1, -0.25],
#                           [0, -0.25, 0]])

    kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                           [-1,  1,  2,  1, -1],
                           [-1,  2,  8,  2, -1],
                           [-1,  1,  2,  1, -1],
                           [-1, -1, -1, -1, -1]])

    
    
    
    def __init__(self):
        FrameRunner.Runner.__init__(self, 30.0)
        
        
        self.__capture = cv2.VideoCapture(0)
#        
#        fileStr = "C:\\Users\\yj_7u\\Pictures\\Icon.bmp"
#        image = cv2.imread(fileStr, 0)
#        cv2.imshow("bluredImg", image)
#        cv2.waitKey(5000)
#        cv2.destroyAllWindows()
#        print("init")
        
    def onUpdateFrame(self):
        suc, frame = self.__capture.read()
        
        #imageGrey =       cv2.cvtColor(frame, imageGrey, cv2.CV)
        #cv.CvtColor(im, res2, cv.CV_RGB2BGR)
        
        imageGrey = frame
        imageB = frame[:,:,0]
        imageG = frame[:,:,1]
        imageR = frame[:,:,2]
        
        imageX = (0.11*imageB + 0.59*imageG+ 0.3*imageR)
        #imageGrey[:,:,0] = imageGrey[:,:,1] = imageGrey[:,:,2] = (0.11*imageB + 0.59*imageG+ 0.3*imageR)
        
#        k3B = ndimage.convolve(imageB, self.kernel_5x5)
#        k3G = ndimage.convolve(imageG, self.kernel_5x5)
#        k3R = ndimage.convolve(imageR, self.kernel_5x5)
        k3img = ndimage.convolve(imageX, self.kernel_5x5)
        
        #imageGrey[:,:,0] = imageGrey[:,:,1] = imageGrey[:,:,2] = (0.11*k3B + 0.59*k3G+ 0.3*k3R) 
        
        imageGrey[:,:,0] = imageGrey[:,:,1] = imageGrey[:,:,2] = k3img #(k3B + k3G+ k3R) / 3
        #imageGrey[:,:,0] = (k3B[:,:,0]+ k3G[:,:,0]+k3R[:,:,0]) / 3
#        imageGrey[:,:,1] = k3G
#        imageGrey[:,:,2] = k3R
        
        
        if(suc):
            print("-----frmage----")
            cv2.imshow("bluredImg", imageGrey)
        else:
            print("-------------------------------------------failed")
        
        #runner.Stop()
        
        return
    
    def onExitFrame(self, frameRemainSec):
        sleepTime = frameRemainSec*1000.0
        
        if(sleepTime<0):
            sleepTime = 1
        
        print( str(frameRemainSec) + '  -----  ' + str(sleepTime))
        keyRet = cv2.waitKey(int(sleepTime))
        if keyRet in range(20,200):
            cv2.destroyAllWindows()
            self.Stop()
            
        print( "##########################" + str(keyRet))


renderer = SimpleRenderer()

def calcSqrt():
    print("888")
    for i in range(0, 100000):
            #np.sqrt(10000)
            #cv2.sqrt(10000)
            math.sqrt(10000.0)

renderer.Run()


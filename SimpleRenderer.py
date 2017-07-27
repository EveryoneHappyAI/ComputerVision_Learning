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
import time
import numpy as np
import math
import FrameRunner
        
        
#class SimpleRenderer:
#    __maxFrameRate = 60
#    __frameLength = 0   # second
#    
#    #__lastFrame
#    
#    def __init__(self, maxFrameRate = 60.0):
#        self.__maxFrameRate = maxFrameRate
#        self.__frameLength = 1.0 / self.__maxFrameRate
#    #def debugFrame
#    
#    def start(self):
#        frmStartTime = time.perf_counter()
#        print("------------------------")
#        
#        #time.
#        print( self.__maxFrameRate, "  ---  ", self.__frameLength)
#        #do sth...
#        
#        for i in range(0, 100000):
#            #np.sqrt(10000)
#            #cv2.sqrt(10000)
#            math.sqrt(10000.0)
#        
#        elapse = time.perf_counter() - frmStartTime
#        timeleft = self.__frameLength - elapse
#        
#        print('' + str(timeleft) + "   " + str(elapse) )
#        if timeleft>0:
#            time.sleep(timeleft)        
#        

renderer = FrameRunner.Runner()

def calcSqrt():
    print("888")
    for i in range(0, 100000):
            #np.sqrt(10000)
            #cv2.sqrt(10000)
            math.sqrt(10000.0)

renderer.Run(calcSqrt)


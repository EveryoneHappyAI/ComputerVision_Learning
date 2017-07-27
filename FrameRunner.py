# -*- coding: utf-8 -*-
"""
FrameRunner 帧运行器

可以设置帧率的运行器，一个框架
Created on Thu Jul 27 17:52:26 2017

@author: yf
"""

import time

class Runner:
    __maxFrameRate = 60
    __frameLength = 0   # second
    __Running = False

    def __init__(self, maxFrameRate = 60.0):
        self.__maxFrameRate = maxFrameRate
        self.__frameLength = 1.0 / self.__maxFrameRate
        self.__Running = False
        
    def Stop(self):
        self.__Running = False
        
    def Run(self, frameFunc):
        self.__Running = True
        
        print("------------------------")
        
        #time.
        print( self.__maxFrameRate, "  ---  ", self.__frameLength)
        
        while self.__Running:
            frmStartTime = time.perf_counter()    
            
            frameFunc()
            
            elapse = time.perf_counter() - frmStartTime
            timeleft = self.__frameLength - elapse
            
            print('' + str(timeleft) + "   " + str(elapse) )
            if timeleft>0:
                time.sleep(timeleft)
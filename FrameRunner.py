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
    __frmStartTime = 0

    def __init__(self, maxFrameRate = 60.0):
        self.__maxFrameRate = maxFrameRate
        self.__frameLength = 1.0 / self.__maxFrameRate
        self.__Running = False
        self.__frmStartTime = 0
        
    def __getFrameElapse(self):
        return time.perf_counter() - self.__frmStartTime
    
    def __getFrameRemain(self):
        return self.__frameLength - (time.perf_counter() - self.__frmStartTime)
        
    def Stop(self):
        self.__Running = False
       
    def onUpdateFrame(self):
        return
    
    def onExitFrame(self, frameRemainSec):
        return
    
    def Run(self, frameFunc):
        return
        
    def Run(self):
        self.__Running = True
        
        print("------------------------")
        
        #time.
        print( self.__maxFrameRate, "  ---  ", self.__frameLength)
        
        while self.__Running:
            self.__frmStartTime = time.perf_counter()    
            
            self.onUpdateFrame()
          
            timeleft = self.__getFrameRemain()
            
            self.onExitFrame(timeleft)
            
            timeleft = self.__getFrameRemain()
            
            print('' + str(timeleft))
            if timeleft>0:
                time.sleep(timeleft)
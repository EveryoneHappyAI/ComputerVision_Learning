# -*- coding: utf-8 -*-
"""

OpenCV 3 学习示例

Camera捕捉图像

Created on Thu Jul 20 18:02:52 2017

@author: yj_7u
"""

import cv2
import time



clicked = False

def onMouse(evt, x, y, flags, param):
    global clicked
    if(evt==cv2.EVENT_LBUTTONDBLCLK):
        clicked = True
        
        
windowName = 'CameraShower'

capturer = cv2.VideoCapture(0)

cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, onMouse)

#suc = capturer.grab()
#frame = capturer.retrieve()

suc, frame=capturer.read()

print(suc)
#help(capturer.read)
help(cv2.waitKey)
while not clicked and suc:    
#    frame = capturer.retrieve()
#    suc = capturer.grab()
    suc, frame=capturer.read()
    
    
    frame = cv2.GaussianBlur(frame, (25, 25), 0)
    
    cv2.imshow(windowName, frame)
    cv2.waitKey(20)


capturer.release()
cv2.destroyWindow(windowName)

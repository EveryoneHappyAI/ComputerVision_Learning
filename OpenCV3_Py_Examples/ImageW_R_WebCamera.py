# -*- coding: utf-8 -*-
"""
OpenCV 3 学习示例

基本的图像结构、读取写入的方法
以及使用Camera视频捕捉的功能

Created on Mon Jul 10 15:58:39 2017

@author: yf
"""

import cv2
#import numpy as np

from skimage import io

#fileStr = "C:\\Users\\yj_7u\\Pictures\\Icon.bmp"
#fileStr = "C:\\Users\\006\\Pictures\\tx.jpg"
fileStr = "C:\\Users\\006\\Pictures\\half.jpg"

image = cv2.imread(fileStr)
testImage = image.copy()


image[0:50,:,2] = 255
#cv2.waitKey()



#----------------------------
# Switch Blue Channel between Red Channel test,OpenCV Reversed
testImage = image.copy()
testImage[:,:,2] ^= testImage[:,:,0]
testImage[:,:,0] ^= testImage[:,:,2] 
testImage[:,:,2] ^= testImage[:,:,0]

#print(image[0])
#print("----------------------------------------------")
#print(testImage[0])
#---------------------------

io.imshow(testImage)


print(image.shape)
print(image.size)
print(image.dtype)


cv2.imshow("TestImg", image)
cv2.waitKey()
#cv2.imshow("TestImg", testImage)
#cv2.waitKey()
cv2.destroyAllWindows()
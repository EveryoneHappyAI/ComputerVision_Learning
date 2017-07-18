# -*- coding: utf-8 -*-
"""
OpenCV 3 学习示例

基本的图像结构、读取写入的方法
以及使用Camera视频捕捉的功能

Created on Mon Jul 10 15:58:39 2017

@author: yf
"""

import cv2
import numpy as np

from skimage import io

fileStr = "C:\\Users\\yj_7u\\Pictures\\Icon.bmp"
#fileStr = "C:\\Users\\006\\Pictures\\tx.jpg"

image = cv2.imread(fileStr)

testImage = image.copy()

testImage[:,:,2] ^= testImage[:,:,0]
testImage[:,:,0] ^= testImage[:,:,2] 
testImage[:,:,2] ^= testImage[:,:,0]

print(image[0])
print("----------------------------------------------")
print(testImage[0])

io.imshow(image)

io.imshow(testImage)



#cv2.imshow("TestImg", image)
#cv2.waitKey()
#cv2.imshow("TestImg", testImage)
#cv2.waitKey()
#cv2.destroyAllWindows()
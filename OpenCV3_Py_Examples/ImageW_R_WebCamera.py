# -*- coding: utf-8 -*-
"""
OpenCV 3 学习示例

基本的图像结构、读取写入的方法
以及使用Camera视频捕捉的功能

Created on Mon Jul 10 15:58:39 2017

@author: yf
"""

import cv2

from skimage import io

image = cv2.imread("C:\\Users\\006\\Pictures\\tx.jpg")

print(image)

io.imshow(image)

cv2.imshow("TestImg", image)
cv2.waitKey()
cv2.destroyAllWindows()
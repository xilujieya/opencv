#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 20:55
# @Author  : pat
# @FileName: 01_hello.py
# @Software: PyCharm

import cv2

print(cv2.getVersionString())

image = cv2.imread("../1.png")
print(image.shape)

cv2.imshow("image", image)
cv2.waitKey(0)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 22:06
# @Author  : pat
# @FileName: 05_均值滤波.py
# @Software: PyCharm

import cv2
import numpy as np

image = cv2.imread("kato.jpg")
# 添加椒盐噪声
for i in range(20000):
    temp_x = np.random.randint(0, image.shape[0])
    temp_y = np.random.randint(0, image.shape[1])
    image[temp_x][temp_y] = 255
# 添加高斯噪声
noise = np.random.normal(0, 1, image.shape)
dst = np.uint8(image + noise)


gauss = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(image, 5)

cv2.imshow("dst", dst)
cv2.imshow("gauss", gauss)
cv2.imshow("median", median)
cv2.waitKey(0)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 21:13
# @Author  : pat
# @FileName: 03_裁剪.py
# @Software: PyCharm

import cv2

image = cv2.imread("kato.jpg")

# 先横后纵
crop = image[10:500, 50:400]
cv2.imshow("crop", crop)

cv2.waitKey(0)
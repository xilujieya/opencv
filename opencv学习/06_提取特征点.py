#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 22:24
# @Author  : pat
# @FileName: 06_提取特征点.py
# @Software: PyCharm

import cv2
import numpy as np

image = cv2.imread("kato.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.01, 10)
for (corner) in corners:
    x, y = corner[0]
    cv2.circle(image, (int(x), int(y)), 3, (0, 0, 255), 1)

cv2.imshow("img", image)
cv2.waitKey(0)

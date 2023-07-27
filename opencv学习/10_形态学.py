#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 21:56
# @Author  : pat
# @FileName: 10_形态学.py
# @Software: PyCharm

import cv2
import numpy as np

gray = cv2.imread("kato.jpg", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # 反向阈值
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(binary, kernel, iterations=1)  # 腐蚀
dilation = cv2.dilate(binary, kernel, iterations=1)  # 膨胀

opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 开运算
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # 闭运算

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.waitKey(0)

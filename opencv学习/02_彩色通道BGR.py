#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 21:02
# @Author  : pat
# @FileName: 02_彩色通道BGR.py
# @Software: PyCharm

import cv2

im = cv2.imread("kato.jpg")

cv2.imshow("BLUE", im[:, :, 0])
cv2.imshow("GREEN", im[:, :, 1])
cv2.imshow("RED", im[:, :, 2])

# 灰度处理，三通道做平方和加权平均
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)



cv2.waitKey(0)
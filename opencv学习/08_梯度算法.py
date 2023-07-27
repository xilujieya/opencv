#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 18:51
# @Author  : pat
# @FileName: 08_梯度算法.py
# @Software: PyCharm

import cv2

gray = cv2.imread("kato.jpg", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey(0)

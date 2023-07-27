# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 21:48
# @Author  : pat
# @FileName: 09_阈值算法.py
# @Software: PyCharm

import cv2

gray = cv2.imread("kato.jpg", cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
#自适应阈值
binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)

ret1, binary_ostu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("binary_adaptive", binary_adaptive)
cv2.imshow("binary_ostu", binary_ostu)
cv2.waitKey(0)
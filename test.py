#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/4 22:33
# @Author  : pat
# @FileName: test.py
# @Software: PyCharm

import cv2

img = cv2.imread("1.png")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)

if __name__ == '__main__':
    pass
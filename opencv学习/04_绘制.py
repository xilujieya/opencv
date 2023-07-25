#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 21:15
# @Author  : pat
# @FileName: 04_绘制.py
# @Software: PyCharm

import cv2
import numpy as np

image = np.zeros([512, 512, 3], dtype=np.uint8)

cv2.line(image, (100, 10), (51, 511), (255, 0, 0), 5)
cv2.rectangle(image, (100, 100), (300, 250), (0, 255, 0), 2)
cv2.circle(image, (300, 300), 50, (0, 0, 255), 4)
cv2.putText(image, "Hello World", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)

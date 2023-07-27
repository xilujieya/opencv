#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 22:34
# @Author  : pat
# @FileName: 07_模板匹配.py
# @Software: PyCharm

import cv2
import numpy as np

image = cv2.imread("poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = gray[320:410, 547:622]

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
location = np.where(result > 0.9)

w, h = template.shape[0:2]
for pt in zip(*location[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("template", template)
cv2.imshow("image", image)
cv2.waitKey(0)
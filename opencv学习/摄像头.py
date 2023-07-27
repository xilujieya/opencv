#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 22:01
# @Author  : pat
# @FileName: 摄像头.py
# @Software: PyCharm

import cv2

capture = cv2.VideoCapture(0)  # 0是代表摄像头编号，只有一个的话默认为0

while True:
    ref, frame = capture.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
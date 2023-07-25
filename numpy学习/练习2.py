#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 13:56
# @Author  : pat
# @FileName: 练习2.py
# @Software: PyCharm

# 图片RGB格式，拼接矩阵

import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

num_9 = mpimg.imread('9_1.png')
print(num_9.shape)
num_5 = mpimg.imread('5_1.png')
print(num_5.shape)
num_1 = mpimg.imread('1_1.png')
print(num_1.shape)

# 拼接为形状：（RGB，宽，高）
num_rgb = np.array([num_9, num_5]).astype(int)
print(num_rgb.shape)

# 交换数轴（宽度，高度，RGB）
num_rgb = np.moveaxis(num_rgb, [0, 1, 2], [2, 0, 1])
print(num_rgb.shape)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 11:35
# @Author  : pat
# @FileName: 练习1.py
# @Software: PyCharm

# 图像的处理：导入图片、翻转、旋转
import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

# 导入图片
num_9 = mpimg.imread('9_1.png')
print(num_9.shape)

plt.matshow(num_9, cmap="Greys_r", vmin=0, vmax=256)
plt.show()

# 左右翻转
# number_lr = np.fliplr(num_9)
number_lr = num_9[:, ::-1]
plt.matshow(number_lr, cmap="Greys_r", vmin=0, vmax=256)
plt.show()

# 上下翻转
# number_ud = np.flipud(num_9)
number_ud = num_9[::-1, :]
plt.matshow(number_ud, cmap="Greys_r", vmin=0, vmax=256)
plt.show()

# 旋转90度
number_rot = np.rot90(num_9, k=3)
plt.matshow(number_rot, cmap="Greys_r", vmin=0, vmax=256)
plt.show()
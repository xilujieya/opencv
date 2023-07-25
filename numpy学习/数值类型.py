#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 21:06
# @Author  : pat
# @FileName: 数值类型.py
# @Software: PyCharm

import numpy as np

# Broadcasting：运算传播机制
# 自动补齐缺失维度（在维度为1的地方复制数组）
arr1 = np.array([[1, 2], [3, 4]])
# （1,2）：一行两列
vec2 = np.array([0, 2]).reshape(1, -1)
# （2，1）：两行一列
vec1 = np.array([0, 2]).reshape(-1, 1)
print(arr1 * vec1)
print(arr1 * vec2)

# numpy的数值形式为自动推导
# 不同数据格式/类型
mat = np.arange(4).reshape(2, 2)
print(mat)
print(mat.dtype)
mat = mat - 1.1
print(mat)
print(mat.dtype)
mat = mat + (1 + 1j)
print(mat)
print(mat.dtype)
# 数据类型强制转换
mat = mat.astype(np.float64)
print(mat)
mat = mat.astype(np.int32)
print(mat)
mat = mat.astype(np.bool)
print(mat)
print(mat.dtype)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 22:33
# @Author  : pat
# @FileName: 数组创建与维度.py
# @Software: PyCharm

# 导入包
import numpy as np

# 列表转化为array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr.shape)
print(arr)

# 创建整数数列
# 类比：list(range(10))
arr = np.arange(10)
print(arr.shape)
print(arr)

# 类比：list(range(0,10,2.5))
# （起始值，终止值，步长）
# [起始值，终止值）范围内步长为间隔的更新
arr = np.arange(0, 10, 2.5)
print(arr.shape)
print(arr)

# 在一个区间内生成等差数列
arr1 = np.linspace(1, 101, 5)
print(arr1.shape)
print(arr1)

# 不包括右区间的值
arr2 = np.linspace(1, 101, 5, endpoint=False)
print(arr2.shape)
print(arr2)

# 取对数后的等距差值
# 10^1=10,10^2=100
arr3 = np.logspace(0, 2, 5, endpoint=True)
print(arr3.shape)
print(arr3)

# 从一维到多维
# 将列表转化为矩阵
mat = np.mat([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(mat.shape)
print(mat)
# 默认：数轴越靠前，变化越快
mat = mat.reshape(3, 3)
print(mat.shape)
print(mat)
# 增加第三个维度
mat = mat.reshape(3, 3, 1)
print(mat.shape)
print(mat)

# 矩阵的初始化：填充矩阵
arr1 = np.zeros((2, 2))
arr2 = np.ones((2, 4))
print(arr1.shape)
print(arr1)
print(arr2.shape)
print(arr2)

arr3 = np.full((2, 2), -np.inf)
arr4 = np.full((2, 2), [1, 2])
print(arr3.shape)
print(arr3)
print(arr4.shape)
print(arr4)

# 使用ones_like()返回矩阵
x = np.arange([[1, 2, 3]])
ones_1 = np.ones_like(x)
ones_2 = np.ones_like(x.shape)
print(x)
print(ones_1)
print(ones_2)

# identity matrix
I = np.identity(3)
print(I)
I_rect = np.eye(3, M=5)
print(I_rect)

# 特殊矩阵：np.triu/np.tril:上三角/下三角矩阵
# 合并/简化矩阵维度（np.flatten/np.ravel/np.squeeze）
# 交换数轴的先后顺序（np.transpose/np.swapaxes）

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/9 20:06
# @Author  : pat
# @FileName: 矩阵选取与运算.py
# @Software: PyCharm

# 导入包
import numpy as np

# 矩阵的拼接
a = np.array((1, 2, 3))
b = np.array((4, 5, 6))
print(a)
print(b)

print(a.shape, b.shape)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

# 矩阵的拼接
print(a.shape)
a = a.reshape(1, -1)
b = b.reshape(1, -1)
print(a.shape)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

print(np.concatenate((a, b, b), axis=0))
print(np.concatenate((a, b, b), axis=1))

# np.hstack/np.vstack:矩阵的横向/纵向拼接
mat = np.arange(9).reshape(3, 3)
print(mat)
# 选择左上角2*2矩阵
print(mat[:2, :2])
# 选择第一列
print(mat[:, 0])
print(mat[:, 0].shape)
# 选择第一列和第三列的所有内容
print(mat[:, [0, 2]])

# np.diag():提取对角线元素;slicing:选择内容（可类比列表选择）
mat = np.arange(9).reshape(3, 3)
print(mat)
# 提取对角线元素
print(np.diag(mat))
print(np.diag(mat).shape)

# 选择内容：按位置；分布选择
# 选取第1/3行，第1/3列的元素
print(mat[[0, 2], :][:, [0, 2]])

# np.where:两种使用方法（替换值、返回索引）
print(mat)
# 用法1：只保留所有大于4的值1，<4的值替换为0
print(np.where(mat > 4, mat, 0))
# 用法2：根据条件选取特定的值
inds_gt4 = np.where(mat > 4)
print(inds_gt4)
print(mat[inds_gt4])
print(mat[mat > 4])

# numpy中常用的常量
# np.inf:无穷大
# np.nan:无效值
# np.pi:圆周率
# np.e:自然常数
# np.euler_gamma:欧拉常数
# np.none

# 按位函数运算：加减乘除
mat = np.arange(0, 4).reshape(2, 2)
print(mat)
print(mat + 1)  # np.add(mat, 1)
print(mat - 1)
print(mat * 2)  # np.multiply(mat, 2)
print(mat / 2)
print(np.exp(mat))
print(np.sin(mat))
print(np.power(mat, 2))


# 单个数组不同位置间的函数运算
mat = np.arange(0, 1, 2, 3, 4).reshape(2, 2)
print(mat)
print(np.sum(mat))
print(np.sum(mat, axis=0))
print(np.sum(mat, axis=1))
print(np.cumsum(mat))
print(np.cumsum(mat, axis=0))

# 数组（向量）之间的运算：按位相乘|向量内积|向量外积
vec1 = np.arange([1, 2])
vec2 = np.arange([2, 1])
# 按位置相乘
print(vec1 * vec2)
# 矩阵内积
print(np.dot(vec1, vec2))
# 矩阵外积
print(np.outer(vec1, vec2))
# 精确定义的乘法运算
print(np.matmul(vec1, vec2))
print(vec1 @ vec2)
print(np.matmul(vec1.reshape(-1, 1), vec2.reshape(1, -1)))
print(vec1.reshape(-1, 1) @ vec2.reshape(1, -1))



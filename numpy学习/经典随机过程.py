#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 23:13
# @Author  : pat
# @FileName: 经典随机过程.py
# @Software: PyCharm


"""经典的随机过程问题之一是随机游走（Random Walk）。随机游走是一个简单的数学模型，描述在一系列随机步骤中，
一个物体在空间中的随机移动。在每一步中，物体可以向左或向右移动一定的距离（或以其他方式定义的步长），而移动方向和步长都是随机确定的。"""

# 使用 NumPy 来模拟一个简单的一维随机游走：


import numpy as np
import matplotlib.pyplot as plt


def random_walk(num_steps):
    # Define the possible step sizes (left and right)
    step_sizes = [-1, 1]

    # Initialize the position at the origin
    position = 0
    positions = [position]

    # Perform the random walk
    for _ in range(num_steps):
        # Randomly choose a step size
        step = np.random.choice(step_sizes)

        # Update the position
        position += step

        # Add the current position to the list of positions
        positions.append(position)

    return positions


# Parameters
num_steps = 100

# Simulate the random walk
positions = random_walk(num_steps)

# Plot the random walk
plt.figure(figsize=(10, 5))
plt.plot(range(num_steps + 1), positions)
plt.xlabel('Number of Steps')
plt.ylabel('Position')
plt.title('Random Walk')
plt.grid(True)
plt.show()

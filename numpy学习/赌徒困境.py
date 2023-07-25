#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 23:07
# @Author  : pat
# @FileName: 赌徒困境.py
# @Software: PyCharm

"""赌徒困境（Gambler's Ruin）问题是一个经典的概率问题，用于描述两名赌徒进行赌博的情境。
假设两名赌徒，A 和 B，开始时各自有一定数量的赌注，它们依次进行赌博，每一轮赌博后，赢家获得一定数量的赌注。
问题的目标是确定在一系列赌博后，其中一名赌徒将会将另一名赌徒的所有赌注都夺走的概率。"""

# 在这个问题中，我们假设赌徒 A 和赌徒 B 分别有初始赌注金额 stake_A 和 stake_B，
# 每次赌博的赌注金额 bet_amount，以及每次赌博获胜的概率 win_prob_A（对于赌徒 A）。


import numpy as np


def gamble(stake_A, stake_B, bet_amount, win_prob_A, num_simulations):
    win_count_A = 0

    for _ in range(num_simulations):
        current_stake_A = stake_A
        current_stake_B = stake_B

        while current_stake_A > 0 and current_stake_B > 0:
            # A wins the bet
            if np.random.rand() < win_prob_A:
                current_stake_A += bet_amount
                current_stake_B -= bet_amount
            # B wins the bet
            else:
                current_stake_A -= bet_amount
                current_stake_B += bet_amount

        # Check if A has won all of B's money
        if current_stake_A == stake_A + stake_B:
            win_count_A += 1

    return win_count_A / num_simulations


# Parameters
stake_A = 50  # Initial stake for gambler A
stake_B = 50  # Initial stake for gambler B
bet_amount = 10  # The bet amount for each round
win_prob_A = 0.5  # The probability of gambler A winning a round
num_simulations = 10000  # Number of simulations to run

win_probability = gamble(stake_A, stake_B, bet_amount, win_prob_A, num_simulations)
print(f"The estimated probability of gambler A winning all of B's money: {win_probability:.4f}")

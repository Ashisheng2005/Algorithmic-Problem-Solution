#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/22 下午2:38 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P2392.py
# @desc : README.md

n = list(map(int, input().split()))
t = 0

mp = [list(map(int, input().split())) for i in n]

for i in range(4):

    _sum = sum(mp[i])

    dp = [0 for i in range(_sum//2 + 1)]

    for j in range(n[i]):
        for k in range(_sum // 2, mp[i][j] - 1, -1):
            dp[k] = max(dp[k], dp[k - mp[i][j]] + mp[i][j])

    t += _sum - dp[_sum//2]

print(t)

# 不懂，找个时间在研究
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/20 下午4:27 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1077.py
# @desc : README.md

# no AC
n, m = map(int, input().split())
mp = list(map(int, input().split()))
mp.insert(0, 0)
dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(m + 1):
        for k in range(min(j, mp[i]) + 1):
            dp[i][j] = (dp[i][j] + dp[i][j - k]) % 1000007


from tool import two_dimensions
two_dimensions(dp)

print(dp[n][m])

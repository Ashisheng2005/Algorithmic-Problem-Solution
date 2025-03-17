#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/13 下午10:50 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1048.py
# @desc : README.md



n, m = map(int, input().split())

w = [0 for _ in range(m+1)]
v = [0 for _ in range(m+1)]
dp = [[0 for _ in range(n+1)] for i in range(m + 1)]

for i in range(1, m+1):
    _w, _v = map(int, input().split())
    w[i] = _w
    v[i] = _v

for i in range(1, m+1):
    for j in range(n, -1, -1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])

        else:
            dp[i][j] = dp[i-1][j]


print(dp[m][n])

# AC
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/17 下午1:14 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P18025.py
# @desc : README.md

n, x = map(int, input().split())

group = [list(map(int, input().split())) for _ in range(n)]
group.sort(key=lambda x: x[2])
# dp = [[0 for i in range(x + 1)] for j in range(n+1)]
dp = [0 for i in range(x + 1)]
for i in range(n):

    for j in range(x, group[i][2] - 1, -1):
        dp[j] = max(dp[j] + group[i][0], dp[j - group[i][2]] + group[i][1])

    for j in range(group[i][2]-1, -1, -1):
        dp[j] += group[i][0]

print(dp[x] * 5)



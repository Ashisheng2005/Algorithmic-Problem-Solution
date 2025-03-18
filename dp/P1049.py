#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/17 下午10:18 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1049.py
# @desc : README.md

v = int(input())
n = int(input())
group = [int(input()) for i in range(n)]
group.sort()

dp = [0 for _ in range(v + 1)]

for i in range(n):

    for j in range(v, group[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - group[i]] + group[i])

# print(dp)
print(v - dp[v])



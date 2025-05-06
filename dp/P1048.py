#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/13 下午10:50 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1048.py
# @desc : README.md

# n, m = map(int, input().split())
#
# w = [0 for _ in range(m+1)]
# v = [0 for _ in range(m+1)]
# dp = [[0 for _ in range(n+1)] for i in range(m + 1)]
#
# for i in range(1, m+1):
#     _w, _v = map(int, input().split())
#     w[i] = _w
#     v[i] = _v
#
# for i in range(1, m+1):
#     for j in range(n, -1, -1):
#         if j >= w[i]:
#             dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
#
#         else:
#             dp[i][j] = dp[i-1][j]
#
#
# print(dp[m][n])

# AC


# t, m = map(int, input().split())
# mp = [list(map(int, input().split())) for i in range(m)]
# dp = [[0 for i in range(t + 1)] for j in range(m)]
#
# for i in range(m):
#
#     for j in range(t, -1, -1):
#         # 从大到小比较，因为这样可以最大程度减少差值
#         if j >= mp[i][1]:
#             dp[i][j] = max(dp[i - 1][j - mp[i][0]] + mp[i][1], dp[i-1][j])
#
#         else:
#             dp[i][j] = dp[i - 1][j]
#
# from tool import two_dimensions
# two_dimensions(dp)
#
# print(dp[-1][-1])



















t, m = map(int, input().split())
mp = [list(map(int, input().split())) for i in range(m)]
dp = [[0 for _ in range(t + 1)] for j in range(m)]

for i in range(m):
    for j in range(t, -1, -1):
        if j >= mp[i][0]:

            dp[i][j] = max(dp[i-1][j - mp[i][0]] + mp[i][1], dp[i-1][j])

        else:
            dp[i][j] = dp[i-1][j-1]


print(dp[-1][-1])



































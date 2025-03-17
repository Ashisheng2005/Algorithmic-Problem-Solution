#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/15 上午9:35 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

import heapq

n, m = map(int, input().split())
ln = sorted(list(map(int, input().split())))
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         dp[i][j] = dp[i - 1][j]
#         for k in range(i):
#             if j % a[i - 1] == 0:
#                 new_j = j
#                 dp[i][j] = max(dp[i][j], dp[k][new_j] + 1)
#
# print(max(dp[n]))

heapq.heapify(ln)

score = 0
while len(ln) > 1:
    x = heapq.heappop(ln)
    y = heapq.heappop(ln)
    if m * x >= y and m * y >= x:
        score += 1
        heapq.heappush(ln, x + y)

    else:
        heapq.heappush(ln, max(x, y))

print(score)

# result = []
# i, j = 0, 0
#
# while i < len(ln):
#     _ln = [j for j in ln]
#     _result = 0
#     j = i + 1
#     while j < len(_ln):
#         if m * _ln[i] >= _ln[j] and m * _ln[j] >= _ln[i]:
#             _ln.append(_ln[i] + _ln[j])
#             _result += 1
#             del _ln[j]
#             del _ln[i]
#
#         else:
#             j += 1
#
#     result.append(_result)
#     i += 1

# print(max(result))
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/20 下午5:30 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P3842_TJOI2007.py
# @desc : README.md
# no AC

# 这个是惯性思想，实际上不符合算法要求，还会有很多的可能星没有考虑到 挂两个点，拿72分
# n = int(input())
# row = [tuple(map(int, input().split())) for i in range(n)]
# row.append((n, n))
#
# count = 0
# now = 1
# for i in range(n + 1):
#     l, r = row[i]
#     if now <= l:
#         count += r - now
#         now = r
#
#     elif now >= r:
#         count += now - l
#         now = l
#
#     else:
#         if now - l <= r - now:
#             count += (now - l) * 2 + (r - now)
#             now = r
#
#         else:
#             count += (r - now) * 2 + (now - l)
#             now = l
#
# print(count + n - 1)

# 普遍的解法还是用dp来解
# 线性dp, 代码抄的，没看懂，我是菜狗
# 每一行的先对必须走完，所以当某一行走完的时候定位一定是在选段最左端或者最右端，向下移动也会占用一次移动机会
# dp[i][0] 表示走线段左侧的路径数量，dp[i][1] 表示走线段右侧的路劲，
# 首先判断第一行的可信性， 然后依次向下递推，每次都判断从左边和从右边走的最短路劲

def dis(x, y):
    return abs(x - y)


n = int(input())
a = [[0, 0] for i in range(n + 1)]
dp = [[0, 0] for i in range(n + 1)]
b = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    a[i][0], a[i][1] = map(int, input().split())
    b[i] = a[i][1] - a[i][0]

dp[1][1] = dis(a[1][1], 1)
dp[1][0] = dis(a[1][1], 1) + b[1]
for i in range(2, n + 1):
    dp[i][0] = min(dp[i -1][0] + b[i] + dis(a[i - 1][0], a[i][1]), dp[i - 1][1] + b[i] + dis(a[i - 1][1], a[i][1])) + 1
    dp[i][1] = min(dp[i -1][0] + b[i] + dis(a[i - 1][0], a[i][0]), dp[i - 1][1] + b[i] + dis(a[i - 1][1], a[i][0])) + 1
print(min(dp[n][0] + dis(n, a[n][0]), dp[n][1] + dis(n, a[n][1])))


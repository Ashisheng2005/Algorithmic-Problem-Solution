#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/6 下午8:46 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1619.py
# @desc : README.md

n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]

cout = []

def fun(value, row, column):
    # 递归方法
    if row == n-1:
        cout.append(value + mp[row][column])
        cout.append(value + mp[row][column + 1])

    else:
        fun(value + mp[row][column], row+1, column)
        fun(value + mp[row][column + 1], row+1, column + 1)

# fun(mp[0][0], 1, 0)
# print(max(cout))


def fun2():
    # 递推方法,没写出啦
    # mp.append([0] * 1000)
    ans = 0
    dp = [[0 for _ in range(1000)] for i in range(1000)]
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + mp[i-1][j-1]
            if dp[i][j] > ans:
                ans = dp[i][j]

    return ans

# print(fun2())

#二维动态规划
# n = int(input())
#
# mp = [list(map(int, input().split())) for a in range(n)]
# for i in range(n-2, -1, -1):
#     for j in range(i + 1):
#         mp[i][j] += max(mp[i + 1][j], mp[i + 1][j + 1])
#
# print(mp[0][0])


def donggui():
    # 一维动态规划
    f = [0 for i in range(n+1)]
    f[1] = mp[0][0]
    for i in range(2, n+1):
        for j in range(i, 0, -1):
            f[j] = max(f[j], f[j-1]) + mp[i-1][j-1]

    ans = max(f)
    return ans

print(donggui())





#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/22 上午10:19 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1216.py
# @desc : README.md


# 这是非动规的方法，由下向上递推， 也能AC，但这一次主要学DP，所以再写一种方法
# n = int(input())
#
# add = []
#
# for i in range(n):
#     add.append(list(map(int, input().split())))
#
# reslut = []
# def foot(add):
#     for i in range(len(add[-2])):
#         if add[-1][i] > add[-1][i+1]:
#             add[-2][i] += add[-1][i]
#
#         else:
#             add[-2][i] += add[-1][i+1]
#
#     del add[-1]
#
# while len(add) != 1:
#     foot(add)
#
# print(add[0][0])


# 有点四不像哈哈
n = int(input())

mp = [list(map(int, input().split())) for a in range(n)]
for i in range(n-2, -1, -1):
    for j in range(i + 1):
        mp[i][j] += max(mp[i + 1][j], mp[i + 1][j + 1])

print(mp[0][0])


#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/22 下午11:24 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    x, y = map(int, input().split())
    if x == y:
        ans.append(-1)
        continue

    for k in range(0, 10000):
        if x + y + (2 * k) == (x + k) ^ (y + k):
            ans.append(k)
            break

for i in ans:
    print(i)

# 超时，感觉有规律，但没找出来
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/19 下午11:18 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

num = int(input())
ans = []

for i in range(num):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    result = 0
    k_mp = []
    for i in range(n):
        result += max(l[i], r[i])
        k_mp.append(min(l[i], r[i]))

    k_mp = sorted(k_mp, reverse=True)
    result += sum(k_mp[:k-1]) + 1

    ans.append(result)

for i in ans:
    print(i)
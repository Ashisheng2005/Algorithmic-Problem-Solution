#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/3 下午10:18 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    t = int(input())
    t *= 3
    t = t / 3 * 4
    t /= 2

    ans.append(round(t))

for i in ans:
    print(i)

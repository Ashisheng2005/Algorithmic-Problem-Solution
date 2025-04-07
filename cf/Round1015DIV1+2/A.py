#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午10:23 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md


n = int(input())

ans = []
for i in range(n):
    s = int(input())
    if s % 2 == 0:
        ans.append(-1)

    else:
        ans.append(f"{s} {' '.join([str(j) for j in range(1, s)])}")

for i in ans:
    print(i)
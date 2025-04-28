#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/24 下午10:17 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

def mex(*arg):
    for i in range(99999):
        if i not in arg:
            return i

num = int(input())

ans = []
for i in range(num):
    n, x = map(int, input().split())
    anss = []
    for j in range(0, x):
        anss.append(j)

    for j in range(n-1, x-1, -1):
        anss.append(j)

    ans.append(anss)

for i in ans:
    print(" ".join(map(str, i)))


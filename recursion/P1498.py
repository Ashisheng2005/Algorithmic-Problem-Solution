#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/10 下午7:05 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1498.py
# @desc : README.md

n = int(input())
a = [1 for i in range(1030)]
i = 0
while i <1<<n:
    i+=1

    j = 1
    while (j < (1<<n)-i):
        j+=1
        print(" ", end="")

    j = i

    while (j>=0):
        j -= 1
        a[j] ^= a[j-1]

    if not i % 2:
        j = 0
        while j <= i:
            j += 1
            print("/\\" if a[j] else "  ", end="")
    else:
        for j in range(0, i+1, 2):
            print("/__\\" if a[j] else "    ", end="")

    print()
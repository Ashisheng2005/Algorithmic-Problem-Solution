#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/19 下午10:46 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

num = int(input())
ans = []

for i in range(num):
    n = int(input())
    t = input()
    data = [0] * n
    big = n
    small = 1
    index = n-1

    for _ in t[::-1]:
        if _ == ">":
            data[index] = big
            big -= 1

        else:
            data[index] = small
            small += 1

        index -= 1

    data[index] = small

    ans.append(data)

for i in ans:
    print(" ".join(map(str, i)))


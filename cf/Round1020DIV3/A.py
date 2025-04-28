#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/24 下午10:17 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md
n =int(input())

ans = []

for i in range(n):
    num = int(input())
    s = input()
    sm = 0

    for j in range(num):
        if s[j] == "1":
            sm += s.count("1") - 1

        else:
            sm += s.count("1") + 1

    ans.append(sm)

for i in ans:
    print(i)
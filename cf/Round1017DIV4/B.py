#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/13 下午11:38 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

num = int(input())

ans = []
for i in range(num):
    n, m, l, r = map(int, input().split())

    left = 0
    right = 0
    for j in range(m):
        if l < left:
            left -= 1

        elif r > right:
            right += 1

    ans.append((left, right))

for i in ans:
    print(i[0], i[1])
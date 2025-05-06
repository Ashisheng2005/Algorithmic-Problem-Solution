#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/1 下午1:49 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

num = int(input())

ans = []

for i in range(num):
    a, b, t = map(int, input().split())

    if (a + b + t) % 3 != 0:
        ans.append("NO")
        continue

    x = (a + b + t) // 3
    ans.append("YES" if b <= x else "NO")


for i in ans:
    print(i)

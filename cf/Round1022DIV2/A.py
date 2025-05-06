#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/1 下午10:51 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

num = int(input())

ans = []
for i in range(num):
    n = int(input())
    cout = 1
    sm = 0
    for j in range(n, -1, -1):
        sm += abs(j - cout)
        cout += 1
    cout = 0
    for _ in range(2, sm + 1, 2):
        cout += 1
    ans.append(cout)

for i in ans:
    print(i)
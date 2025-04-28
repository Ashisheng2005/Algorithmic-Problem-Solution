#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/21 下午11:09 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

num = int(input())

ans = []
for i in range(num):
    n = int(input())
    a = input().strip()
    cnt = 0
    for i in range(n - 1):
        if a[i] != a[i + 1]: cnt += 1
    if cnt == 0:
        ans.append(n + int(a[0] == "1"))
    elif cnt == 1:
        ans.append(n + 1)
    else:
        ans.append(n + cnt - 1 - int(a[0] == "0" and cnt > 2))

for i in ans:
    print(i)

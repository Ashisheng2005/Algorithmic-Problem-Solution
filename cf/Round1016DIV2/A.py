#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/8 下午10:35 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    k = int(input())
    if k % 2 == 1:
        ans.append("yes")

    else:
        ans.append('no')

for i in ans:
    print(i)

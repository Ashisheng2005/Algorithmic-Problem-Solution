#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/21 下午10:59 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

num = int(input())
ans = []

for i in range(num):
    m = int(input())
    mp = list(map(int, input().split()))
    len_mp = len(set(mp))
    ans.append(len_mp)

for i in ans:
    print(i)
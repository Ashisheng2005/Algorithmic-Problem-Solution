#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/13 下午11:36 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    name = input().split(" ")
    _name = ""
    for k in name:
        _name += k[0]

    ans.append(_name)

for i in ans:
    print(i)
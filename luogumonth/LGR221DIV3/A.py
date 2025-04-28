#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/19 下午1:57 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

n, t = map(int, input().split())

asn = 0

start = 0
for i in range(n):
    s, e = map(int, input().split())
    if start < s:
        if s - start > t:
            asn += s - start - t

    start = e

print(asn)

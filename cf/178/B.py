#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/1 下午2:08 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

num = int(input())
ans = []

for i in range(num):
    n = int(input())
    mp = list(map(int, input().split()))
    mp.sort(reverse=True)
    _ans = [mp[0]]
    for item in mp[1:]:
        _ans.append(_ans[-1] + item)

    ans.append(_ans)

for i in ans:
    print(" ".join(map(str, i)))

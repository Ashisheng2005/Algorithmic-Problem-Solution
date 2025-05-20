#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/19 下午9:18 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P3613.py
# @desc : README.md

# 读取输入
n, q = map(int, input().split())
lockers = {}
ans = []
for _ in range(q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        _, i, j, k = op
        if i not in lockers:
            lockers[i] = {}
        lockers[i][j] = k
    else:
        _, i, j = op
        ans.append(lockers.get(i, {}).get(j, 0))

for i in ans:
    print(i)
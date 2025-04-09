#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/8 下午10:40 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    t = input()
    del_zero = 0
    # 计算右边的0的个数
    del_zero += len(t) - len(t.rstrip("0"))
    if del_zero > 0:
        t = t[:-1 * del_zero]
    left_count = len(t) - t.count("0") - 1
    left_count = max(0, left_count)
    ans.append(left_count + del_zero)

for i in ans:
    print(i)

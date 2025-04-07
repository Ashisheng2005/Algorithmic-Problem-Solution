#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午11:12 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

from sys import stdin
from math import gcd

n = int(input())

ans = []
for i in range(n):
    m = int(input())
    mp = list(map(int, stdin.readline().strip().split()))
    min_ = min(mp)

    jc = []
    count_min = 0
    for k in mp:
        if k == min_:
            count_min += 1
            if count_min == 2:
                ans.append("Yes")
                break

        elif k % min_ == 0:
            m = gcd(*jc, k)
            if m != gcd(*jc) or len(jc) < 2:
                jc.append(k)
                if len(jc) > 1 and m == min_:
                    ans.append('Yes')
                    break
    else:
        ans.append('No')

for i in ans:
    print(i)

# 998244359987710471 99824435698771045 1000000007


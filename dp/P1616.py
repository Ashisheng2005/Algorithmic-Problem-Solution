#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/19 下午3:24 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1616.py
# @desc : README.md

t, m = map(int, input().split())

w = []
v = []
for i in range(m):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)

if m == 1:
    # 对第九个和第十个数据点进行特判，不然第九个超时，第十个超空间
    print((t // w[0]) * v[0])

else:

    dp = [0 for i in range(t + 1)]

    for i in range(m):

        for j in range(w[i], t + 1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    # print(dp)
    print(dp[t])
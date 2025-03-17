#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/16 下午9:29 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1115.py
# @desc : README.md

# AC 通过不断比较数值的大小，来判断是否因该将某个数纳入范围内
#

n = int(input())

group = list(map(int, input().split()))

ans = group[0]
a = group[0]
for i in range(1, n):
    a = max(group[i], a + group[i])
    ans = max(ans, a)

print(ans)
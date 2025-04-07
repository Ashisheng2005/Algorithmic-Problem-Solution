#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午2:13 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : C.py
# @desc : README.md

# 内嵌反推斐波那契

def n_f(n, a=1, b=1):
    # n前的系数
    a, b = a, b
    for i in range(n - 1):
        a, b = b, a + b
    return a


n = int(input())
ans = []

for i in range(n):
    a, x, b = map(int, input().split())
    if a == 1:
        ans.append(n_f(b, a=x, b=x+1))
        continue

    elif a == 2:
        ans.append(n_f(b, a=x-1, b=x))
        continue

    y = (x - n_f(a-1)) / n_f(a)
    if y%1 == 0:
        ans.append(int(n_f(b, a=y, b=y+1)))
    else:
        ans.append(-1)

for i in ans:
    print(i)


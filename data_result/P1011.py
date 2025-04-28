#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/25 下午11:30 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1011.py
# @desc : README.md

def fibnq(n):
    a, b = 1, 1
    if n <= 2:
        return 1

    for i in range(2, n):
        a, b = b, a + b

    return b


a, n, m, x = map(int, input().split())
if x <= 2:
    print(a)

elif x == 3:
    print(2 * a)
    
else:
    f_n = fibnq(n)
    a2 = (m - (f_n * a)) / (f_n - 1)
    f_x = fibnq(x)
    print(f_x * a + (f_x - 1) * a2)


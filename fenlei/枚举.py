#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/5 下午9:48 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : 枚举.py
# @desc : README.md

# 求数组中和为0的两个数
ans = [1,0,2,-5,-6,-8,5,6]

for i in range(len(ans)):
    for j in range(len(ans)):
        if ans[i] + ans[j] == 0:
            print(f"{ans[i]}, {ans[j]}")

# 若无位置要求，可以将第一个位置设置为考前，优化为

for i in range(len(ans)):
    for j in range(i):
        if ans[i] + ans[j] == 0:
            print(f"{ans[i]}, {ans[j]}")

# 上述两种算法都会输出a,b和b,a，重复了一次，如果没有要求，则可以



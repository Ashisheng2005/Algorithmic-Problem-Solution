#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/17 下午2:39 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P2404.py
# @desc : README.md

def cout(b):
    for i in range(b):
        if i == 0:
            print(a[i], end="")

        else:
            print(f"+{a[i]}", end="")

    print()
    return


def dfs(x, y, z):
    if x == n: return
    if y == n:
        cout(z)
        return
    for i in range(x, n-y+1):
        a[z] = i
        dfs(i, y+i, z+1)


n = int(input())
a = [0 for i in range(9)]
dfs(1, 0, 0)
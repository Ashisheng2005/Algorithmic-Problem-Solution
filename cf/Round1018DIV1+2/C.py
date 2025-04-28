#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/19 下午11:53 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : C.py
# @desc : README.md

def shpw(data):
    for i in data:
        print(" ".join(map(str, i)))


num = int(input())

ans = []

for i in range(num):
    n = int(input())
    mp = [list(map(int, input().split())) for j in range(n)]
    a_computer = list(map(int, input().split()))
    b_computer = list(map(int, input().split()))

    for x in range(n):
        for y in range(n):
            if mp[x][y] == mp[x][y + 1]:
                pass

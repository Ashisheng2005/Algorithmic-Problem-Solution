#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/13 下午9:48 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1004.py
# @desc : README.md

n = int(input()) + 1
Map = [[0] * n] * n

while True:
    x, y, value = map(int, input().split())
    if x == y ==value == 0: break
    Map[x][y] = value

result = []

def foot(x, y, value):
    try:
        value += Map[x][y]

    except IndexError:
        print(x, y, value)

    if x == y == n:
        result.append(value)

    elif x == n and y < n:
        foot(x, y+1, value)

    elif x < n and y == n:
        foot(x + 1, y, value)

    else:
        foot(x + 1, y, value)
        foot(x, y + 1, value)

n -= 1
foot(1, 1, 0)
print(sorted(result))
print(sum(sorted(result)[:2]))





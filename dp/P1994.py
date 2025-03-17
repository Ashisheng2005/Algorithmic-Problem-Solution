#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/13 下午10:31 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1994.py
# @desc : README.md

n = int(input())

add = []

for i in range(n):
    add.append(list(map(int, input().split())))

reslut = []
def foot(add):
    for i in range(len(add[-2])):
        if add[-1][i] > add[-1][i+1]:
            add[-2][i] += add[-1][i]

        else:
            add[-2][i] += add[-1][i+1]

    del add[-1]

while len(add) != 1:
    foot(add)

print(add[0][0])

# AC

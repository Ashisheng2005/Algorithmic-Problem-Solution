#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/19 下午10:08 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1996.py
# @desc : README.md

n, m = map(int, input().split())
mp = [i for i in range(1, n+1)]
ans = []

eip = 1
index = 0
while len(mp) > 0:

    if eip == m:
        ans.append(mp[index])
        mp[index] = False
        eip = 0

    eip += 1
    index += 1

    if index == len(mp):
        index = 0

        while False in mp:
            del mp[mp.index(False)]

print(" ".join(map(str, ans)))


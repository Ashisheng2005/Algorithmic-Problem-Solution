#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/16 下午11:59 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1019.py
# @desc : README.md

def dfs(data, length):
    for i in range(n):
        if type_mp[i] != 2:
            for j in range(min(len(data), len(mp[i])) - 1, 0, -1):
                if data[-j:] == mp[i][:j]:
                    type_mp[i] += 1
                    dfs(mp[i], length + len(mp[i]) - j)
                    type_mp[i] -= 1
                    break

    else:
        lengths.append(length)


n = int(input())
lengths = []
mp = [input() for i in range(n)]
type_mp = [0 for _ in range(n)]
head = input()

for i in range(n):
    if head == mp[i][0]:
        type_mp[i] += 1
        dfs(mp[i], len(mp[i]))
        type_mp[i] -= 1

print(max(lengths))



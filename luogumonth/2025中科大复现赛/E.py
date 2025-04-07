#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午3:53 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : E.py
# @desc : README.md

def get(node, c_num):
    if node in lod.keys():
        return lod[node]

    c





n, m = map(int, input().split())
root = {}

for i in list(map(int, input().split())):
    root[i+1] = i

mp = list(map(int, input().split()))
for i in range(n):
    root[i] = (root[i], mp[i])

lod = {}
max_num = 0



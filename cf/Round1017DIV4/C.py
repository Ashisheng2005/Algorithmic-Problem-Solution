#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/13 下午11:53 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : C.py
# @desc : README.md
n = int(input())

ans = []

for i in range(n):
    num = int(input())
    ans_list = []
    mp = []
    for k in range(num):
        mp.append(list(map(int, input().split())))

    for x in range(num):
        if x == 0:
            ans_list.extend(mp[x])
        else:
            ans_list.append(mp[x][-1])

    for item in range(1, 2*num+1):
        if item not in ans_list:
            ans_list.insert(0, item)
            break
    ans.append(ans_list)

for i in ans:
    print(" ".join(map(str, i)))


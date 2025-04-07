#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/3 下午10:46 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md

n = int(input())

ans = []

for i in range(n):
    n, k, x = map(int, input().split())
    mp = list(map(int, input().split()))
    _sum = 0
    count = 0
    for x in range(0, n):
        for y in range(x, n+1):
            _sum += mp[y]
            if _sum >= x:
                count += 1
                break

        for y in range(0, x):
            _sum += mp[y]
            if _sum >= x:
                count += 1
                break

    ans.append(count * k//2)

    # 存在n段个原生mp数组
    # for j in range(n+1, n*k+1):
    #     mp.append(mp[i-n])
    #
    # print(mp)

for i in ans:
    print(i)
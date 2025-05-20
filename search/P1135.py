#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/12 下午1:03 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1135.py
# @desc : README.md

def dfs(a, num):
        print(a)
        global flag

        if flag:
            return

        if a == b:
            print(num)
            flag = True

        if mp[a-1] == 0:
            return

        if a + mp[a - 1] <= n and dfsl_bool[a-1][0]:
            dfs(a + mp[a-1], num+1)

        else:
            dfsl_bool[a - 1][0] = False

        if a - mp[a-1] >= 0 and dfsl_bool[a-1][1]:
            dfs(a - mp[a-1], num+1)

        else:
            dfsl_bool[a-1][1] = False


n, a, b = map(int, input().split())
mp = list(map(int, input().split()))
dfsl = [(a, 0)]
flag = False
dfsl_bool = [[True, True] for i in range(n)]

dfs(a, 0)
print(dfsl_bool)
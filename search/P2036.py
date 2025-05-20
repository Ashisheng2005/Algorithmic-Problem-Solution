#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/15 下午8:31 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P2036.py
# @desc : README.md

def dfs(i, x, y):
    global ans
    if i == n:
        if x == 1 and y == 0: return
        ans = min(ans, abs(x-y))
        return

    dfs(i + 1, x*mp[i][0], y+mp[i][1])
    dfs(i+1, x, y)


n = int(input())
mp = [list(map(int, input().split())) for i in range(n)]
ans = float('inf')
dfs(0, 1, 0)
print(ans)

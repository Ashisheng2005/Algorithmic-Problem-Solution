#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/16 下午8:06 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1605.py
# @desc : README.md

def dfs(x, y):
    # print(x, y)
    if not mp[x][y]:
        return

    global ans

    if x == fx and y == fy:
        ans += 1
        return

    mp[x][y] = 0

    if x+1 <= n and mp[x+1][y]:
        dfs(x+1, y)

    if x-1 >= 1 and mp[x-1][y]:
        dfs(x - 1, y)

    if y + 1 <= m and mp[x][y+1]:
        dfs(x, y+1)

    if y - 1 >= 1 and mp[x][y-1]:
        dfs(x, y-1)

    mp[x][y] = 1


n, m, t = map(int, input().split())
sx, sy, fx, fy = map(int, input().split())
mp = [[1 for i in range(n+1)] for j in range(m+1)]
ans = 0
for i in range(t):
    x, y = map(int, input().split())
    mp[x][y] = False
dfs(sx, sy)

print(ans)
# for i in mp:
#     print(" ".join(map(str, i)))



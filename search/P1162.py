#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/18 上午10:21 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1162.py
# @desc : README.md

def dfs(x, y):
    if x >= n or y >= n or x < 0 or y < 0 or mp[x][y] != 0:
        return

    if (x == 0 or y == 0 or x == n-1 or y == n-1) and mp[x][y] == 0:
        mp[x][y] = 2
        return True

    d = dfs(x+1, y)
    if d:
        mp[x][y] = 2
        return True

    d = dfs(x - 1, y)
    if d:
        mp[x][y] = 2
        return True

    d = dfs(x, y + 1)
    if d:
        mp[x][y] = 2
        return True

    d = dfs(x, y - 1)
    if d:
        mp[x][y] = 2
        return True


n = int(input())
mp = [list(map(int, input().split())) for i in range(n)]

for i in mp:
    for j in range(n):
        if i[j] == 2:
            print(0, end=" ")

        elif i[j] == 0:
            print(2, end=" ")

        else:
            print(1, end=" ")

    print()

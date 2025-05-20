#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/18 上午9:18 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1596.py
# @desc : README.md

def dfs(x, y, number):
    if mp[x][y] == "W":
        mp[x][y] = number

        if x + 1 < n:
            dfs(x + 1, y, number)

        if y + 1 < m:
            dfs(x, y+1, number)

        if x - 1 >= 0:
            dfs(x-1, y, number)

        if y - 1 >= 0:
            dfs(x, y-1, number)

        if x - 1 >= 0 and y - 1 >= 0:
            dfs(x-1, y-1, number)

        if x - 1 >= 0 and y + 1 < m:
            dfs(x-1, y+1, number)

        if x + 1 < n and y + 1 < m:
            dfs(x+1, y+1, number)

        if x + 1 < n and y - 1 >= 0:
            dfs(x+1, y-1, number)


n, m = map(int, input().split())
number = 0
# mp = [list(input()) for i in range(n)]
mp = []
flag = True
for i in range(n):
    mp2 = input()
    if "." in mp2:
        flag = False
    mp.append(list(mp2))


if flag:
    print(1)
    # 全为W，会超出最大栈
else:
    for i in range(n):
        for j in range(m):
            if mp[i][j] == "W":
                dfs(i, j, number)
                number += 1

    print(number)

# for i in mp:
#     print("".join(map(str, i)))

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/15 上午10:54 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : SHOL2002_P1434.py
# @desc : README.md

# AC
# 读取输入
# R, C = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(R)]
#
# # dp 数组，初始化为 0，表示未计算
# dp = [[0] * C for _ in range(R)]
#
# # 四个方向：上、下、左、右
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# # DFS + 记忆化
# def dfs(x, y):
#     # 如果已经计算过，直接返回
#     if dp[x][y] != 0:
#         return dp[x][y]
#
#     # 初始长度为 1（当前点）
#     dp[x][y] = 1
#
#     # 检查四个方向
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 边界检查 && 海拔降低条件
#         if (0 <= nx < R and 0 <= ny < C and grid[nx][ny] < grid[x][y]):
#             dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
#
#     return dp[x][y]
#
#
# # 从每个点开始计算最长路径
# ans = 0
# for i in range(R):
#     for j in range(C):
#         ans = max(ans, dfs(i, j))
#
# # 输出结果
# print(ans)


R, C = map(int, input().split())
table = [[map(int, input().split())] for i in range(R)]
dp = [[0] * C for j in range(R)]

_x = [0, 0, -1, 1]
_y = [-1, 1, 0, 0]


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + _x[i]
        ny = y + _y[i]

        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] < table[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


ans = 0
for i in range(R):
    for j in range(C):
        ans = max(ans, dfs(i, j))

print(ans)










































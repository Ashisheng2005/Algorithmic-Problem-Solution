#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/15 下午9:43 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P4017.py
# @desc : README.md

# n, m = map(int, input().split())
# result = {}
#
# for i in range(m):
#     _, __ = map(int, input().split())
#     if _ in result:
#         result[_].append(__)
#
#     else:
#         result[_] = [__]
#
# _result = {}
#
#
# def dfs(index):
#     if index not in result.keys():
#         return 1
#
#     if index in _result.keys():
#         return _result[index]
#
#     _len = 0
#     for i in result[index]:
#         _len += dfs(i)
#
#     _result[index] = _len
#
#     return _len
#
#
# ans = dfs(min(result.keys()))
#
# print(ans)

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
out_degree = [0] * (n + 1)
dp = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
    out_degree[a] += 1

queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        dp[i] = 1
        queue.append(i)

MOD = 80112002
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        dp[neighbor] = (dp[neighbor] + dp[current]) % MOD
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

result = 0
for i in range(1, n + 1):
    if out_degree[i] == 0:
        result = (result + dp[i]) % MOD

print(result)



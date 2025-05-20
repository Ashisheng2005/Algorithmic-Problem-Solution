#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/14 下午8:56 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P2196.py
# @desc : README.md

# 通过逆推方法，自后向前判断选择，并且记录路径，最后在mp中选择总值最大的，输出完整路径和最大值
#
# n = int(input())
# mp = list(map(int, input().split()))
# row = []
# road = [[] for i in range(n)]
# for i in range(n-1):
#     row.append(list(map(int, input().split())))
#
#
# # print(mp)
# # print(row)
# for i in range(n-2, -1, -1):
#     _max = 0
#     _max_load = []
#     for j in range(len(row[-1])):
#         if row[-1][j] == 1:
#             if mp[i + j + 1] > _max:
#                 _max_load = []
#                 _max = mp[i + j + 1]
#                 for item in road[i + j + 1]:
#                     _max_load.append(item)
#                 _max_load.append(i + j + 2)
#
#     for item in _max_load:
#         road[i].append(item)
#
#     mp[i] += _max
#     del row[-1]
#
# # print(mp)
# # print(road)
#
# _m_value = max(mp)
# _index = mp.index(_m_value)
# road[_index].append(_index + 1)
# print(" ".join(map(str, sorted(road[_index]))))
# print(mp[_index])


# AC

n = int(input())
vp = list(map(int, input().split()))
ap = [list(map(int, input().split())) for i in range(n-1)]

dp = [_ for _ in vp]
for i in range(n-2, -1, -1):
    for j in range(len(ap[i])):
        if ap[i][j] == 1:
            dp[i+1] = max(dp[i] + dp[i+1:][j], dp[i+1])
            # print(dp)


print(max(dp))



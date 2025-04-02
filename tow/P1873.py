#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/31 下午10:19 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1873.py
# @desc : README.md


# 排序，二分

n, m = map(int, input().split())
mp = list(map(int, input().split()))
m_mp = max(mp)

left = 0
right = 0
while left <= m_mp:
    mid = (left + m_mp) // 2
    s = 0
    for i in range(n):
        if mp[i] > mid:
            s += mp[i] - mid

    if s < m:
        m_mp = mid - 1

    else:
        left = mid + 1

print(left - 1)

# #2 #3 #10 超时 TLE




# 最小前缀和
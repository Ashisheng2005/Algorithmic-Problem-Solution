#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/25 上午12:05 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : D.py
# @desc : README.md

num = int(input())
INF = 1e9 + 5
ans = []
for i in range(num):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    j = n - 1
    #
    backwards_match = [0 for i in range(m)]

    for i in range(m-1, -1, -1):
        while j >= 0 and a[j] < b[i]:
            j -= 1

        backwards_match[i] = j
        j -= 1

    forwards_match = [0 for i in range(m)]
    j = 0
    for i in range(0, m):
        while j < n and a[j] < b[i]:
            j += 1

        forwards_match[i] = j
        j += 1

    if forwards_match[-1] < n:
        ans.append(0)
        continue

    _ans = INF
    for i in range(0, m):
        match_previous = -1 if i ==0 else forwards_match[i - 1]
        match_next = n if i + 1 == m else backwards_match[i + 1]
        if match_next > match_previous:
            _ans = min(_ans, b[i])

    ans.append(-1 if _ans == INF else _ans)


for i in ans:
    print(i)



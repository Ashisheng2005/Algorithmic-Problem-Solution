#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/20 下午5:30 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P3842_TJOI2007.py
# @desc : README.md
# no AC

n = int(input())
row = [tuple(map(int, input().split())) for i in range(n)]
row.append((n, n))

count = 0
now = 1
for i in range(n + 1):
    l, r = row[i]
    if now <= l:
        count += r - now
        now = r

    elif now >= r:
        count += now - l
        now = l

    else:
        if now - l <= r - now:
            count += (now - l) * 2 + (r - now)
            now = r

        else:
            count += (r - now) * 2 + (now - l)
            now = l

print(count + n - 1)

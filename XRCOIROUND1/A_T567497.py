#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/15 下午2:45 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A_T567497.py
# @desc : README.md

# 1 2 2 2 3 4

n = int(input())
dp = []
for i in range(n):
    value, count = map(int, input().split())
    for _ in range(count):
        dp.append(value)

dp.sort()

# _dp = [i - 1 if i-1>=0 else None for i in dp]
_dp = [0]

for i in range(1, len(dp)):
    value = _dp[-1] + 1
    for j in range(i):
        if value < dp[i]:
            _dp.append(value)
            break
        else:
            value += 1

    else:
        _dp.append(-dp[-1])

if None in _dp:
    print(-1)

else:
    for i in range(1, len(_dp)):
        if _dp[i-1] > _dp[i]:
            print(-1)
            break
    else:
        print(len(_dp))
        print(" ".join(map(str, _dp)))
        
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/23 下午10:43 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : C.py
# @desc : README.md

def check_prefix_and_middle(n, arr):
    # 检查前缀和中间

    suf = [0] * (n + 1)
    minsuf = [0] * (n + 1)
    suf[n] = minsuf[n] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suf[i + 1] = suf[i + 2] + arr[i]
        minsuf[i + 1] = min(minsuf[i + 2], suf[i + 1])

    s = 0
    for i in range(n - 2):
        s += arr[i]
        if s < 0:
            continue
        if suf[i + 2] >= minsuf[i + 3]:
            return True

    return False


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # 根据k的值变换数组
    for i in range(n):
        arr[i] = 1 if arr[i] <= k else -1

    a, b = n + 1, -1
    s = 0

    for i in range(n):
        s += arr[i]
        if s >= 0:
            a = i + 1
            break

    s = 0
    for i in range(n - 1, -1, -1):
        s += arr[i]
        if s >= 0:
            b = i + 1
            break

    if a + 1 < b:
        return "YES"

    if check_prefix_and_middle(n, arr):
        return "YES"

    arr.reverse()

    if check_prefix_and_middle(n, arr):
        return "YES"

    return "NO"


t = int(input())
ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(i)
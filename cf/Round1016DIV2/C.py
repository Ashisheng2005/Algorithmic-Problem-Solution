#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/8 下午10:58 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : C.py
# @desc : README.md

# 基本思路简单，但困难与python时间复杂度太高，不得已使用Miller_rabbin算法，优化，AC

import random

def Miller_Rabbin(n):
    k, p = 0, n - 1
    while (p & 1) == 0:
        p = p >> 1
        k += 1
    for j in range(6):
        a = random.randint(1, n - 1)
        b = pow(a, p, n)
        flag = 0
        if b == 1:
            continue
        for i in range(k):
            if (b + 1) % n == 0:
                flag = 1
                break
            else:
                b = (b * b) % n
        if flag == 1:
            continue
        else:
            return False
    return True


n = int(input())
ans = []

for i in range(n):
    x, k = map(int, input().split())

    x = int(str(x) * k)
    if x == 2:
        ans.append("yes")
        continue

    if x % 2 == 0 or (x == k == 1):
        ans.append("No")
        continue

    if Miller_Rabbin(x):
        ans.append("Yes")
    else:
        ans.append("no")

    # for k in range(3, int(pow(x, 0.5)) + 1, 2):
    #     if x % k == 0:
    #         ans.append("No")
    #         break
    #
    # else:
    #     ans.append("Yes")

for i in ans:
    print(i)


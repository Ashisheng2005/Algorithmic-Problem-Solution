#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/14 上午12:57 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : E.py
# @desc : README.md

def solve(a, n):
    # 统计每位的 0 和 1
    cnt_0 = [0] * 30
    cnt_1 = [0] * 30
    for x in a:
        for j in range(30):
            if (x >> j) & 1:
                cnt_1[j] += 1
            else:
                cnt_0[j] += 1

    # 计算每个 k 的贡献
    max_sum = 0
    for k in range(n):
        current_sum = 0
        for j in range(30):
            # 如果 a[k] 第 j 位为 0，贡献为 cnt_1[j] * 2^j
            # 如果 a[k] 第 j 位为 1，贡献为 cnt_0[j] * 2^j
            if (a[k] >> j) & 1:
                current_sum += cnt_0[j] * (1 << j)
            else:
                current_sum += cnt_1[j] * (1 << j)
        max_sum = max(max_sum, current_sum)

    # print(max_sum)

    return max_sum

n = int(input())

ans = []
for i in range(n):
    num = int(input())
    mp = list(map(int, input().split()))

    result = solve(mp, num)
    ans.append(result)

for i in ans:
    print(i)


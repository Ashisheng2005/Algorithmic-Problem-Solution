#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/24 下午10:17 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : C.py
# @desc : README.md
def change(n):
    if n != "-1":
        return int(n)

    return None


num = int(input())
ans = []
for i in range(num):
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 处理已知元素
    fixed_x = -1
    valid = True
    for i in range(n):
        if b[i] != -1:
            x = a[i] + b[i]
            if fixed_x == -1:
                fixed_x = x
            elif fixed_x != x:
                valid = False

    if not valid:
        ans.append(0)
        continue

    # 处理丢失元素
    min_x = 0
    max_x = float('inf')
    for i in range(n):
        if b[i] == -1:
            min_x = max(min_x, a[i])  # x >= a[i]
            max_x = min(max_x, a[i] + k)  # x <= a[i] + k

    if fixed_x != -1:
        # 已知 x，检查是否合法
        if min_x <= fixed_x <= max_x:
            ans.append(1)
        else:
            ans.append(0)
    else:
        # 没有已知 x，计算 x 的可能个数
        if min_x <= max_x:
            ans.append(max_x - min_x + 1)
        else:
            ans.append(0)


for i in ans:
    print(i)




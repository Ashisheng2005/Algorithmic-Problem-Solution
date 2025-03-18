#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/17 下午10:15 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : A.py
# @desc : README.md

def min_operations(n, k):
    operations = 0
    while n != 0:
        if n % 2 == 0:
            if n <= k:
                operations += 1
                return operations

            j = k if k % 2 == 0 else k-1
            for i in range(1, n, 100 if n > 9999 else 1):
                if i * j > n:
                    operations += i - 100 if n > 999 else 1
                    n -= j * (i - 100 if n > 999 else 1)
                    break

        elif n <= k:
            operations += 1
            break

        else:
            operations += 1
            n -= n//k

    return operations


t = int(input())
group = [list(map(int, input().split())) for i in range(t)]
ans = []
for i in group:
    n, k = i[0], i[1]
    ans.append(min_operations(n, k))

for i in ans:
    print(i)
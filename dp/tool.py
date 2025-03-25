#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/14 下午8:35 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : tool.py
# @desc : README.md

def two_dimensions(item):
    n = len(str(max(item[0]))) + 2
    print(f"$", end="  ")
    for i in range(len(item[0])):
        print(f"{i:>{n}}", end=' ')

    print()
    for i in range(len(item)):
        print(f"#{i}", end=" ")
        for j in item[i]:
            print(f"{j:>{n}}", end=' ')

        print()


if __name__ == '__main__':
    x = [[1,2,3], [4,5,6], [7,8,9]]
    two_dimensions(x)


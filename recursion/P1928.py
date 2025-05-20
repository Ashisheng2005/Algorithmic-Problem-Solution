#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/8 下午9:03 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1928.py
# @desc : README.md

# AC

def recursion(data):
    if not "[" in data:
        if 48 <= ord(data[0]) <= 57:
            if 48 <= ord(data[1]) <= 57:
                return recursion(int(data[:2]) * data[2:])

            return recursion(int(data[0]) * data[1:])

        return data

    left=None
    right=0
    cout = 0
    end = len(data)
    while right < end:
        if data[right] == "[":
            if left is None: left = right
            cout += 1

        elif data[right] == "]":
            cout -= 1
            if cout == 0:
                break

        right += 1

    else:
        return data

    return recursion(data[:left] + recursion(data[left+1:right]) + data[right+1:])


n = input()
print(recursion(n))


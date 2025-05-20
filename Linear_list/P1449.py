#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/19 下午9:36 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1449.py
# @desc : README.md

def add(x, y):
    x, y = int(x), int(y)
    return x + y


def red(x, y):
    x, y = int(x), int(y)
    return x - y


def mul(x, y):
    x, y = int(x), int(y)
    return x * y


def div(x, y):
    x, y = int(x), int(y)
    return int(x / y)


computation = {"+": add, "-":red, "*":mul, "/":div}

number_stack = []
mp = list(input().split("."))
for i in mp:
    if ("*" in i) or ("/" in i) or ("+" in i) or ("-" in i) or ("@" in i):
        temp_num = ""
        for j in i:
            if j in "+-*/":
                if temp_num != "":
                    number_stack.append(temp_num)
                    temp_num = ""
                x, y = number_stack[-2], number_stack[-1]
                del number_stack[-2], number_stack[-1]
                number_stack.append(computation[j](x, y))

            elif j == "@":
                break

            else:
                temp_num += j

        if temp_num != "":
            number_stack.append(temp_num)
            temp_num = ""


    else:
        number_stack.append(i)

print(number_stack[-1])


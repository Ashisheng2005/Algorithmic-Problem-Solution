#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/8 下午10:31 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1259.py
# @desc : README.md

n = int(input())

end_str = "__"
eip = n

def recursion():
    # print(text)
    global n

    if n > 3:
        print(("o" * n) + ("*"*n) + "--" + "o*" * (eip - n))
        n -= 1
        print(("o" * n) + "--" + ("*"*n) + "o*" * (eip - n))
        return recursion()

    else:
        print(("ooo*o**--*") + "o*" * (eip - 4))
        print("o--*o**o" + "o*" * (eip - 3))
        print("o*o*o*--" + "o*" * (eip - 3))
        print("--" + ("o*") * eip)

recursion()



# AC 模拟加递归和分治。。。


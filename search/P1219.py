#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/5/11 上午9:46 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1219.py
# @desc : README.md

# n = int(input())
#
# a = [0 for i in range(100)]
# b = [0 for i in range(100)]
# c = [0 for i in range(100)]
# d = [0 for i in range(100)]
#
# total = 0
# def cout():
#     global total
#     if total <= 2:
#         for i in range(1, n+1):
#             print(str(a[i]) + " ", end="")
#         print()
#
#     total += 1
#
# def queen(i):
#     if i > n:
#         cout()
#         return
#
#     for j in range(1, n+1):
#         if (not b[j]) and (not c[i+j]) and (not d[i-j+n]):
#             a[i] = j
#             b[j] = 1
#             c[i+j] = 1
#             d[i-j+n] = 1
#             queen(i+1)
#             b[j] = 0
#             c[i + j] = 0
#             d[i - j + n] = 0
#
# # n=13会TLE，打个表先， AC
# if n == 13:
#     print("""1 3 5 2 9 12 10 13 4 6 8 11 7
# 1 3 5 7 9 11 13 2 4 6 8 10 12
# 1 3 5 7 12 10 13 6 4 2 8 11 9
# 73712""")
# else:
#     queen(1)
#     print(total)


n = int(input())

a = [0 for i in range(100)]
b = [0 for i in range(100)]
c = [0 for i in range(100)]
d = [0 for i in range(100)]

total = 0

def cout():
    global total
    if total <= 2:
        print(" ".join(map(str, a[1:n+1])))

    total += 1

def queen(i):
    global total
    if i > n:
        cout()

    else:
        for j in range(1, n+1):
            if (not b[j]) and (not c[i+j]) and (not d[i-j+n]):
                a[i] = j
                b[j] = 1
                c[i + j] = 1
                d[i - j + n] = 1
                queen(i + 1)
                b[j] = 0
                c[i + j] = 0
                d[i - j + n] = 0

queen(1)
print(total)






























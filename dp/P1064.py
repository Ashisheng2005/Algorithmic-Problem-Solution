#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/21 下午9:27 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : P1064.py
# @desc : README.md

n, m = map(int, input().split())

mp = [list(map(int, input().split())) for i in range(m)]
mp.sort(key=lambda x:x[2])


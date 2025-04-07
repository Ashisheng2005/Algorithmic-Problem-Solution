#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/4/5 下午1:14 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : B.py
# @desc : README.md
import re


def FindFlag(s):
    if len(s) < 6:
        return "NOT FOUND"

    pattern = r"flag{[^{}]*}"
    matches = re.search(pattern, s)
    return matches.group(0) if matches else "NOT FOUND"


s = input()
print(FindFlag(s))

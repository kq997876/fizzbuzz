#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:02:23 2023

@author: yangkeqing
"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    print(i)
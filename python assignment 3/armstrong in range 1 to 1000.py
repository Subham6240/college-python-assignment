# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:02:14 2020

@author: SUBHAM
"""

for num in range(1,1001):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    if num == sum:
        print(num)
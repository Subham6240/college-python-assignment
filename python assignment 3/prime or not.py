# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:34:23 2020

@author: SUBHAM
"""

num = int(input("enter a number"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        elif(i==num-1):
            print(num, "is a prime number")
            
else:
   print(num, "is not a prime number")
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:33:01 2020

@author: SUBHAM
"""

for num in range(1,1001):
    count=0
    for i in range(2,(num//2 +1)):
        if(num % i ==0):
            count=count+1
            break
    if(count==0 and num !=1):
        print("%d "%num)
            
        
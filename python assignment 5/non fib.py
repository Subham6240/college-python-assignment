# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:06:24 2020

@author: SUBHAM
"""

num=int(input("enter the upper range of fibonacci :"))
a=1
b=0
c=0
while(a+b)<=num:
    c=a+b
    a=b
    for i in range (b+1,c):
        print (i)
    b=c
for i in range(b+1,num+1):
    print(i)
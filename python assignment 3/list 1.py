# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:01:07 2020

@author: SUBHAM
"""

list=[]
e=(int)(input("Enter the no. of elements in the list: "))
for i in range(e):
    n=(int)(input())
    list.append(n)
print("The list:")
for i in range(e):
    print(list[i])
print("No more elements")

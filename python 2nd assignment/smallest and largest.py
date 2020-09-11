# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:29:35 2020

@author: SUBHAM
"""

x=float(input("enter 1st number :"))
y=float(input("enter 2nd number :"))
z=float(input("enter 2nd number :"))
if x>y and x>z :
    print("the largest is :",x)
elif y>z and y>x :
    print("the largest is :",y)
else :
    print("the largest is :",z)
if x<y and x<z :
    print("the smallest is :",x)
elif y<z and y<x : 
    print("the smallest is :",y)
else :
    print("the smallest is :",z)
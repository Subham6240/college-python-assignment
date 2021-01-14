# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:51:19 2021

@author: SUBHAM
"""

def func1(x,y):
    if y<=x:
        return func1(x-y,y)+1
    return 1
def func2(n,r):
    if n>0 or r>0:
        return func2(n-1,r) + func2(n-1,r-1)
    else :
        return 0
def func3(n):
    if n>1:
        return func3(n/2)+1
    return 0
def func4(m,n):
    if m==0 or (m>=n and n>=1):
        return 1
    else:
        return func4(m-1,n)+func4(m-1,n-1)
def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
def func5(m,x):
    if x==0:
        return 1
    if m>x:
        return fact(m)/(fact(x)*fact(m-x))
    else :
        return func5(m,x-1)*((m-x+1)/x)

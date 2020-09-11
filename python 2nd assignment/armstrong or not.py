# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:46:42 2020

@author: SUBHAM
"""

x=int(input("enter a number :"))
k=x
sum=0
num=0
while k>0 :
    num=k%10
    sum=sum+(num**3)
    k=k//10
if sum == x :
    print("armstrong number")
else :
    print("not armstrong")

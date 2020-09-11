# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:37:39 2020

@author: SUBHAM
"""

x=float(input("enter temp."))
u=input("enter unit c/f  ")
if u=='c':
    temp=float((9*x/5)+32)
    print("temp. is",str(temp),"F")
elif u=='f':
    temp=float(5*(x-32)/9)
    print("temp is :",str(temp),"C")
else : print("wrong unit")
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:07:07 2020

@author: SUBHAM
"""

x=float(input("enter score : "))
if x>1.0 or x<0.0:
    print("error")
elif x>0.9 :
    print('A')
elif x>=0.8 and x<0.9:
    print('B')
elif x>=0.7 and x<0.8:
    print("C")
elif x>=0.6 and x<0.7:
    print('D')
else :
    print ("F")
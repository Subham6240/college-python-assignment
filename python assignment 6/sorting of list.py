# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:16:32 2020

@author: SUBHAM
"""

try:
    list = list(input("Enter elements separated by a space: ").split())
    list.sort()
    print("The sorted list is: ", list)
    
except:
    print("Enter homogeneous elements!!")
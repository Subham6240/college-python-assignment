# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:35:17 2020

@author: SUBHAM
"""

try:
    lst1 = list(input("Enter elements separated by a space: ").split())

    frequency = {} 
    for item in lst1: 
        frequency[item] = lst1.count(item) 

    print("Frequencies of the elements are: ")
    for key, value in frequency.items(): 
        print (str(key) + " :  " + str(value))
        
except:
    print("Enter elements seperated by a single space!!")
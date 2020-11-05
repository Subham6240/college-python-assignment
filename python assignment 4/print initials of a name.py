# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:02:49 2020

@author: SUBHAM
"""

s=input("enter a name ")
w=s.split(" ")
reverse=[i[0] for i in w]
new_sent=" ".join(reverse)
print(new_sent)
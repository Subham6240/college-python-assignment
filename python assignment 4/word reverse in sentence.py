# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:00:35 2020

@author: SUBHAM
"""

s=input("enter a sentence ")
w=s.split(" ")
reverse=[i[::-1] for i in w]
new_sent=" ".join(reverse)
print(new_sent)
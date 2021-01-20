# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:42:58 2021

@author: SUBHAM
"""

words=0
with open("file2.txt","r") as f:
       for line in f:
          w=line.split()
          words+=len(w)
max_len=len(max(w,key=len))
print(words)
print(max_len)
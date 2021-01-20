# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:08:06 2021

@author: SUBHAM
"""

f=open("file1.txt","r")
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())
f.seek(0)
print(f.read(5))
f.seek(0)
for x in f :
    print(x)
f.close()

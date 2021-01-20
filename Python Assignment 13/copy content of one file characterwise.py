# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:09:51 2021

@author: SUBHAM
"""

f1=open("file1.txt","r")
lines=f1.readlines()
word=''
for line in lines :
    for ch in line:
        word=word+ch
f1.close()
with open("file69.txt","w") as file:
    for x in word :
        file.write(x)
    
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:47:00 2021

@author: SUBHAM
"""

f1=open("file1.txt","r")
lines=f1.readlines()
new_word=''
for line in lines:
    for ch in line:
        if ch.lower():
            new_word = new_word+ch.upper()
        elif ch.upper():
            new_word = new_word+ch.lower()
        else:
            new_word = new_word+f1.close()
with open("file70.txt",'w') as file :
    for x in new_word:
        file.write(x)
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:16:37 2021

@author: SUBHAM
"""

f = open("file2.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f = open("file2.txt", "r")
print(f.read())

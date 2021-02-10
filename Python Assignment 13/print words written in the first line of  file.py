# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:33:54 2021

@author: SUBHAM
"""

with open("file1.txt", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print(word)
file.close()


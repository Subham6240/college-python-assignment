# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:48:55 2021

@author: SUBHAM
"""

data = data2 = "" 

with open('file1.txt') as fp: 
    data = fp.read() 
    
with open('file2.txt') as fp: 
    data2 = fp.read() 

data += "\n"
data += data2 
  
with open ('file71', 'w') as fp: 
    fp.write(data)
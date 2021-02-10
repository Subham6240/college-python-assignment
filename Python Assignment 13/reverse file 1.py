# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:48:45 2021

@author: SUBHAM
"""

f1 = open("output1.txt", "w") 
  
with open("file1.txt", "r") as myfile: 
    data = myfile.read() 
data_1 = data[::-1] 
f1.write(data_1) 
f1.close() 
f=open("output1.txt","r")
print(f.read())
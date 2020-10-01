# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:57:55 2020

@author: SUBHAM
"""

c=0
while 1:
    try:
        n=input()
        if n=="done":
            break
        else:
            n=int(n)
    except ValueError:
        print("Error! Enter numeric input only.")
    else:
        if c==0:
            max=n
            min=n
        else:
            if n>max:
                max=n
            if n<min:
                min=n
        c=c+1
print("Maximum: "+str(max))
print("Minimum: "+str(min))
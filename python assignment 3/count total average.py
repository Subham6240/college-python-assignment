# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:49:14 2020

@author: SUBHAM
"""

s=0
c=0
while 1:
    try:
        n=input()
        if n=="done":
            break
        else:
            n=int(n)
    except ValueError:
        print("Error!Enter numeric input only")
    else:
        s=s+n
        c=c+1
        print("total:"+str(s))
        print("count:"+str(c))
        print("average:"+str(s/c))
        
    
    
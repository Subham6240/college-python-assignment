# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:49:58 2020

@author: SUBHAM
"""

s= input("enter string")
s=" "+s
w=0;v=0;c=0;p=0
for i in range(len(s)):
    if(s[i]==" "):
        w=w+1
    elif(s[i]=="." or s[i]=="," or s[i]=="?" or s[i]=="!" or s[i]==":" or s[i]=="'"):
        p=p+1
    elif(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" s[i]=="U"):
        v=v+1
    else :
            c=c+1
print("words=",w,"vowels=",v,"consonent=",c,"punctuations=",p)           
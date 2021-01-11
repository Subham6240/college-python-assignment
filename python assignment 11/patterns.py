# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:42:17 2021

@author: SUBHAM
"""

def pypatt1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
        
def pypatt2(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k=k-1
        for c in range(0,i+1):
            print('* ',end='')
        print('\r')
        
def pypatt3(n):
    k=2*n-2
    for i in range (0,n):
        for j in range(0,k):
            print(end=' ')
        k=k-2
        for c in range(0,i+1):
            print('* ',end='')
        print('\r')
        
def pypatt4(n):
    num=1
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end=' ')
            num=num+1
        print('\r')
        
def pypatt5(n):
    num=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=' ')
            num=num+1
        print('\r')
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:51:03 2020

@author: SUBHAM
"""
try:

        row,col = input('Enter number of rows and columns separated by a comma:').split(',')
        table = []
        row = int(row)

        while (row):

            lst = list(map(int,input(f'Enter {col} elements separated by comma:').split(',')))

            if len(lst) != int(col):
                print('Number of columns provided is wrong please try again.')
            
            else:
                row =row- 1
                table.append(lst)
        
        print('\nThe table is:\n')
        for r in table:
            for c in r:
                print(c,end='\t')
            print()
            
             
except:
        print('Wrong input. Try again.')

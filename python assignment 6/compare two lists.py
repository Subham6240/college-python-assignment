# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:29:23 2020

@author: SUBHAM
"""
list1 = input('Enter the first list of items').split(',')
list2 = input('Enter the second list of items').split(',')

if list1 == list2:
    print(f'{list1} and {list2} are equivalent.')
elif list1 > list2:
    print(f'{list1} is greater than {list2}')
else:
    print(f'{list2} is greater than {list1}')

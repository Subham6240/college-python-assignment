# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:39:01 2020

@author: SUBHAM
"""

while (1):

    try:

        s = input('Enter items separated by a comma:').split(',')
        search = input('Enter element to search:')
        found = []
        checked = False
        i = 0

        while not checked:

             try:
                use = s[i:]
                index = use.index(search)
                i = i + index + 1
                found.append(i-1)

             except:
                checked = True

        if len(found) == 0:
            print('No such element is present.')
        
        elif len(found) == 1:
            print(f'The element ({search}) is present in {found[0]} index')

        else:
            lst = list(map(str,found))
            print(f"The element ({search}) is found in {','.join(lst)} indices")
        break
    except:
        print('Wrong input format. try again.')
        
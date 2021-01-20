# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:14:31 2021

@author: SUBHAM

"""
import filecmp
f1='filecmp1.txt'
f2='filecmp2.txt'
comp=filecmp.cmp(f1,f2,shallow=False)
print(comp)

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:31:01 2020

@author: SUBHAM
"""
rate=int(input("Rate :"))
hours=int(input("hours :"))
if hours <= 40:
    pay=hours*rate
else:
    pay=40*rate +1.5*rate*(hours-40)
print("pay:",pay)
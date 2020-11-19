# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:28:59 2020

@author: SUBHAM
"""

try:
    players1= []
    players2=[]
    team=[]
    for i in range (int(input("Enter the number of players  "))):
        players1.append(input("Enter the name: "))
    for i in range (int(input("Enter the number of players  "))):
        players2.append(input("Enter the name: ")) 
    team.append(players1)
    team.append(players2)
    print("the players are",team)
except:
    print("enter valid range")
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:07:51 2021

@author: SUBHAM
"""

import creatures
def display():
    c=int(input("Enter your choice:"))
    while(1):
        if c==1:
            creatures.fish.examples()
            creatures.fish.chars()
            break
        elif c==2:
            creatures.birds.examples()
            creatures.birds.chars()
            break
        elif c==3:
            creatures.amphibians.examples()
            creatures.amphibians.chars()
            break
        elif c==4:
            creatures.mammals.examples()
            creatures.mammals.chars()
            break
        elif c==5:
            creatures.reptiles.examples()
            creatures.reptiles.chars()
            break
        else:
            print("Wrong input.")
            break
    
        
print("Find your information about creatures(example and characteristics)")
print("Chose an option:\n1.Fish\n2.Birds\n3.Amphibians\n4.Mammals\n5.Reptiles\n6.Exit")
display()
while(1):
    print("Do you want to continue?Y/N:")
    k=input()
    if k=='Y':
        display()
    elif k=='N':
        print("THANK YOU!!!")
        break
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:13:28 2021

@author: SUBHAM
"""

import funcs as f
while 1:
    print("Enter the function number (eg:-1 for function 1 and 2 for function 2 and so on )\nPress 6 to exit")
    c = int(input())
    if c == 1:
        print("Enter x and y:")
        x, y = input().split()
        x = int(x)
        y = int(y)
        print("Result=", f.func1(x, y))
    elif c == 2:
        print("Enter n and r:")
        n, r = input().split()
        n = int(n)
        r = int(r)
        print("Result=", f.func2(n, r))
    elif c == 3:
        n = int(input("Enter n:"))
        print("Result=", f.func3(n))
    elif c == 4:
        print("Enter m and n")
        m, n = input().split()
        m = int(m)
        n = int(n)
        print("Result=", f.func4(m, n))
    elif c == 5:
        print("Enter m and x")
        m, x = input().split()
        m = int(m)
        x = int(x)
        print("Result=", f.func5(m, x))
    elif c == 6:
        print("Thanks")
        break
    else:
        print("Wrong input")
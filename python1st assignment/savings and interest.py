#interest and total amount including principle
principle=float(input("enter principle"))
interest=float(input("annual interest "))
years=float(input("years "))
total=principle*years*interest/100
print("total interest is :", total)
gross=total+principle
print("total amount is:", gross)
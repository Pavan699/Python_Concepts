'''
@Author: Pavan Nakate
@Date: 2021-11-01 10:36
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Power of 2 : Print the Power of 2 upto the entered number 
'''
#importing math library to use pow
import math
number = int(input("Enter a range to get the power of two: "))

# Checking if entered range is within the limit.
if(0<number<31):
    for i in range (1,number+1):      # Iteration from 1 to Number
        print("2 ^ ",i," = ",pow(2,i)) 
else:
    print("Enter proper range")

# Without using Pow i.e. using '**'
if(0<number<31):
    for j in range (1,number+1):
        print("2 ^ ",j," = ",2**j)
else:
    print("Enter proper range")
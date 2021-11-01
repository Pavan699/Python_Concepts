'''
@Author: Pavan Nakate
@Date: 2021-11-01 01:07
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Prime Factor : Finding the prime factors of the entered number
'''
# UserInput as Integer number
Number = int(input("Enter a number to get it's prime factors: "))
prime_factors = [] # list to store the factors
factor = 2 

# Looping till the quotient is less than divisor.
while factor <= Number:
    if Number % factor == 0:
        prime_factors.append(factor) # append method to add the factor in list
        Number = Number/factor
    else:
        factor += 1

print("Prime factors are : ",prime_factors)
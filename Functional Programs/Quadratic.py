'''
@Author: Pavan Nakate
@Date: 2021-11-02 01:02
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Quadratic : To find the roots of the quadratic equation  
'''
# importing math to use functions
import math

def quadratic_equation():
    """
    Description:
        In this function the two roots of quadratic equation is found.
        a, b, c are the three inputs to find the delta value.
        The value of delta should be greater than 0 to have two real roots.
    Parameter:
        None
    Return:
        None
    """   

    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    c = int(input("Enter the value of c : "))

    # Getting the value of delta.
    # Formula is delta = b*b - 4*a*c
    delta = (b * b - 4 * a * c)

    # Finding the roots if value of delta is greater than 0.
    if(delta > 0):
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)

        print("First root of equation is : ",root1)
        print("Second root of equation is : ",root2)
    else:
        print("There are no real two roots for the given values")

# Calling function
quadratic_equation() 
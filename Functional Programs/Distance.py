'''
@Author: Pavan Nakate
@Date: 2021-11-02 01:02
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Distance : To calculate the Distance of thr x,y co-ordinates from origin  
'''
# importing math to use the sqrt() and power() functions
import math

def distance():
    """
    Description:
        Print the Euclidean distance from the point (x, y) to the origin (0, 0).
        The formula is distance = sqrt(x**x + y**y) -> by using pow() function
        Printing the distance the ditance
    Parameter:
        None
    Return:
        None
    """   
    
    # Userinput for x and y co-ordinates.
    x = float(input("Enter the value of x-coordinate: "))
    y = float(input("Enter the value of y-coordinate: "))

    # Calculating the distance.
    result = math.sqrt( math.pow(x,2) + math.pow(y,2) )
    print("The distance from the origin for given co-ordinates is: ",result)

# Calling the distance function
distance()
'''
@Author: Pavan Nakate
@Date: 2021-11-03 11:13
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : CouponsNumbers : Print the uniqe coupon numbers 
'''
import random

def coupon_numbers():
    """
    Description:
        Calculate the Unique Coupon numbers
        no. of coupons and range are the user inputs
        coupons array to store the unique coupons
    Parameter:
        None
    Return:
        None
    """   
    # User Inputs
    number_of_coupon = int(input("Enter the number of coupons to print: "))
    coupon_range = int(input("Enter the range of coupon numbers: "))

    coupons = [] # Array to store all coupon numbers.

    for i in range(number_of_coupon):
        random_coupons = random.randint(1,coupon_range)#used random to get the coupons
        coupons.append(random_coupons)

    # Set is used to print unique numbers.
    unique_number = set(coupons)
    print("Unique coupon numbers are: ", unique_number)

if __name__ == "__main__":
    coupon_numbers()
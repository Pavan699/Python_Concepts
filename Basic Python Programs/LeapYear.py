'''
@Author: Pavan Nakate
@Date: 2021-11-01 10:52
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Leap Year : Check the Year is leap year or not
'''
#importing the re(reguler expression) for the validation
import re
Year = input("Enter the Year to check : ")

if re.match("^[0-9]{4}$", Year):
    if int(Year) % 4 == 0:
        if int(Year) % 100 != 0 or int(Year) % 400 == 0:
            print(f"The year {Year} is a leap year")
        else:
            print("Its not a leap year")
    else:
         print("Its not a leap year")
else:
    print("Enter a valid year")
    
'''
@Author: Pavan Nakate
@Date: 2021-11-01 10:52
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Leap Year : Check the Year is leap year or not
'''
#importing the re(reguler expression) for the validation
import re
year = input("Enter the Year to check : ")

if re.match("^[1-9]{1}[0-9]{3}$", year):
    if int(year) % 4 == 0:
        if int(year) % 100 != 0 or int(year) % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print("Its not a leap year")
    else:
         print("Its not a leap year")
else:
    print("Enter a valid year")
    
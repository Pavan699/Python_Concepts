'''
@Author: Pavan Nakate
@Date: 2021-11-01 10:20
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : User Input : Checking the username using regex(reguler expression)
'''
#Program to check the Entered Name is valid or not
#importing the re(reguler expression) for the validation
import re

name = input("Enter the Name : ")#user input

if re.match('^[A-Za-z]{3,}$', name): 
    print(f"Hello {name}, How are you?")
else:
    print("Name is Invalid")

# Fuction in RE ==>
# match() -> function will check the pattern and entered string and return the object(string) if matches 
# findall() -> it returns the list of all the matched contains
# search() -> returns the first object which is matched with the pattern
# split() -> returns a list where the string has been split at each match 

'''
@Author: Pavan Nakate
@Date: 2021-11-01 12:46
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Harmonic Number : To get the harmonic value of entered number
'''
# User Input H_Number and Harmonic_Result to store the result
H_Number = int(input("Enter a range to get harmonic value: "))
Harmonic_Result = 0

if H_Number < 0 or H_Number == 0: #if 0 or less than zero 
    print("Range is invalid")
else:
    for i in range(1,H_Number+1): #iterartion is Starting from 1 
        Harmonic_Result += 1/i
    print(f"Harmonic value of {H_Number} is : ",Harmonic_Result)

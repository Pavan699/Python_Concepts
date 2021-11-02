'''
@Author: Pavan Nakate
@Date: 2021-11-01 12:46
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Harmonic Number : To get the harmonic value of entered number
'''
# User Input H_Number and Harmonic_Result to store the result
harmonic_number = int(input("Enter a range to get harmonic value: "))
harmonic_result = 0

if harmonic_number < 0 or harmonic_number == 0: #if 0 or less than zero 
    print("Range is invalid")
else:
    for i in range(1,harmonic_number+1): #iterartion is Starting from 1 
        harmonic_result += 1/i
    print(f"Harmonic value of {harmonic_number} is : ",harmonic_result)

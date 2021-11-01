'''
@Author: Pavan Nakate
@Date: 2021-11-01 11:13
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Flip-Coin Percentage : Percentage for the Heads and Tails for entered number
'''
# importing random to use the random() function
import random

Number_Of_Toss = int(input("Enter the number of times you want to flip the coin : "))
#Counters for the Head and Tail
tail_count = 0
head_count = 0

for toss in range(Number_Of_Toss):
    toss = random.random() # To generate random numbers from 0.0 to 1.0
    if toss < 0.5:
        print("Tails")
        tail_count += 1
    else:
        print("Heads")
        head_count += 1

# Calculating the percentage of tails and heads.
Tail_Percent = (tail_count/Number_Of_Toss)*100
Head_Percent = (head_count/Number_Of_Toss)*100

print("Tail percentage is ",Tail_Percent)
print("Head percentage is ",Head_Percent)
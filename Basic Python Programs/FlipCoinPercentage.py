'''
@Author: Pavan Nakate
@Date: 2021-11-01 11:13
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Flip-Coin Percentage : Percentage for the Heads and Tails for entered number
'''
# importing random to use the random() function
import random

number_Of_Toss = int(input("Enter the number of times you want to flip the coin : "))
#Counters for the Head and Tail
tail_count = 0
head_count = 0

for toss in range(number_Of_Toss):
    toss = random.random() # To generate random numbers from 0.0 to (0.9)1.0
    if toss < 0.5:
        print("Tails")
        tail_count += 1
    else:
        print("Heads")
        head_count += 1

# Calculating the percentage of tails and heads.
tail_Percent = (tail_count/number_Of_Toss)*100
head_Percent = (head_count/number_Of_Toss)*100

print("Tail percentage is ",tail_Percent)
print("Head percentage is ",head_Percent)
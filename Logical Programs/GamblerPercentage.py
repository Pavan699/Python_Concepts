'''
@Author: Pavan Nakate
@Date: 2021-11-03 10:00
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : GamblerPercentage 
'''
import random

def gambler_game():  
    """
    Description:
        Calculate the Percentage of a gambler.
        The stake and goal are the user inputs.
        Random is used for the win or loss of the player
        Tha main aim is continue this game as stack is reaches at 0 or the goal(entered input)
    Parameter:
        None
    Return:
        None
    """ 
    #try block to check the exception
    try:
        stake = int(input("Enter the stake amount : "))
        goal = int(input("Goal amount to win : "))

        win_count = 0
        loss_count = 0
        num_of_bets = 0

        if(stake > 0 and goal > stake):
            while not(stake == 0 or stake == goal): # Keeps looping until stake is 0 or equal to goal
                bet = random.randint(0,1) # Generates two random numbers 0 and 1              
                num_of_bets += 1

                if bet == 0:
                    stake += 1
                    win_count += 1
                if bet == 1:
                    stake -= 1
                    loss_count += 1
        else:
            print("Enter a valid stake and goal amount")

        print("Number of times Gambler won : ", win_count)
        print("Number of times Gambler lost : ", loss_count)
        print("Total bets placed is : ", num_of_bets)
        print("Current Stack is : ",stake)

        # Calculating win and loss percentage
        win_percentage = (win_count/num_of_bets)*100
        loss_percentage = (loss_count/num_of_bets)*100

        print("Win percentage is: ", win_percentage)
        print("Loss percentage is: ", loss_percentage)
    #Printing Exception if occurs
    except Exception as e:
        print("Exception occured is: ", e)
        
if __name__ == "__main__":
    gambler_game()
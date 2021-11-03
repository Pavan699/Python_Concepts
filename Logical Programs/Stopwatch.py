'''
@Author: Pavan Nakate
@Date: 2021-11-03 11:58
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Stopwatch : Calculate the time between two entred keys 
'''
import time

def stop_watch():
    """
    Description:
        Function is used to simulate stop watch
        Calculate the time-span between two enter buttons
        Use of the time library to calculate the time
    Parameter:
        None
    Return:
        None
    """  

    # To start the timer.
    input("Press Enter to start the timer : ")
    start_time = time.time()

    # To end the timer.
    input("Press Enter to stop the timer : ")
    stop_time = time.time()

    # To get the total elapsed time.
    print("Total elapsed time is: ",stop_time-start_time,"sec ")

if __name__ == "__main__":
    stop_watch()
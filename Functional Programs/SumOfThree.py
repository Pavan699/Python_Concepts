'''
@Author: Pavan Nakate
@Date: 2021-11-02 02:26
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : SumOfThree : find the list of three elements having sum is zero from the given array  
'''
# Parameterised function
def triples(arr, n):
    """
    Description:
        Function which takes input as array and it's length and gives 3 elements having sum is zero
    Parameter:
        arr - represents a input array having elements
        n - represents the length of the array
    Return:
        None
    """   
    flag = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n): 
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k]) #0,-1,1
                    flag = True

    # if flag remains False that means there are no elements having sum with 0
    if (flag == False):
        print("Elements are not exist having thier sum as Zero")
 
# Array with elements and it's length
array_list = [0, -1, 2, -3, 1]
size = len(array_list)
# calling function
triples(array_list, size)
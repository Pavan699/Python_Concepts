'''
@Author: Pavan Nakate
@Date: 2021-11-02 11:27
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Array2D : Print the 2D array by using print function  
'''
#Print Function
def Print():
    """
    Description:
        Print Function to take the input elements and print the 2D-Array
        Userinput as rows , columns and elements for the array
        Print the 2D-Array
    Parameter:
        None
    Block:
        None
    Return:
        None
    """  
    #try to catch the exception if occures  
    try:
        # rows and cloumns for the 2D-array
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        #Array to save the elements
        array_matrix = []
        
        # For loop to get the elements and create 2D-Array.
        for row in range(rows):
            array_elements = [] # to store the small array
            for column in range(columns):
                array_elements.append(int(input("Enter the element : ")))
            array_matrix.append(array_elements)

        # To print the elements.
        print("The 2D array : ")
        for row in range(rows):
            for column in range(columns):
                print(array_matrix[row][column], end=" ")
            print()
            
    except Exception as e:
        print("Exception is: ",e)

if __name__ == "__main__":
    Print()
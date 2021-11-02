'''
@Author: Pavan Nakate
@Date: 2021-11-01 08:10
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : InventoryDataManagment : Convert the json Object form to json string form
'''
# Importing Json library 
import json

## List of json objects

#To read open and read the json file
myjson_file = open('D:\Python\CFP-Class\Object Oriented Programs\Data.json','r')
json_data = myjson_file.read()

#Loading the data by using json.loads method
json_obj = json.loads(json_data) #Data is in Object format

list = json_obj # there are 3 data's present so storing in the list format
print(list)

for i in range(len(list)): #for loop for accessing the objects in list
    print("Details of the item => ")
    print("Name : ",list[i].get('name'))
    print("Weigth : ",list[i].get('weigth'))
    wg = float(list[i].get('weigth')) #conversion of string to float 
    print("Price : ",list[i].get('price'))
    pr = float(list[i].get('price'))  #conversion of string to float
    print("Bill is : ",wg*pr) # calculating bill by using converted values 

#String Format by using dumps
data_str = json.dumps(list)
print(data_str)



## Single Json Object

#open and read the json file 
my_details_file = open('D:\Python\CFP-Class\Object Oriented Programs\Details.json','r')
person_data = my_details_file.read()

person_obj = json.loads(person_data) # Load-String
print("Person Details :")
print("Name :",person_obj['name'])
print("Address :",person_obj['address'])
print("City :",person_obj['city'])
print("Phone No. :",person_obj['phone'])

#dumps => dump-String function
person_str = json.dumps(person_obj)
print(person_str)
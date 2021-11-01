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
myjsonFile = open('D:\Python\CFP-Class\Object Oriented Programs\Data.json','r')
jsondata = myjsonFile.read()

#Loading the data by using json.loads method
Json_Obj = json.loads(jsondata) #Data is in Object format

list = Json_Obj # there are 3 data's present so storing in the list format
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
Detail_Str = json.dumps(list)
print(Detail_Str)



## Single Json Object

#open and read the json file 
myDetailsFile = open('D:\Python\CFP-Class\Object Oriented Programs\Details.json','r')
persondata = myDetailsFile.read()

Person_Obj = json.loads(persondata) # Load-String
print("Person Details :")
print("Name :",Person_Obj['name'])
print("Address :",Person_Obj['address'])
print("City :",Person_Obj['city'])
print("Phone No. :",Person_Obj['phone'])

#dumps => dump-String function
Person_str = json.dumps(Person_Obj)
print(Person_str)
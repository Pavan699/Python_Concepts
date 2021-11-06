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
json_obj = json.loads(json_data) 

list = json_obj # there are 3 data's present so storing in the list format
print(list)
list_cal = [] # list to add the new object with bill

for i in range(len(list)): #for loop for accessing the objects in list
    print("Details of the item => ")
    print("Name : ",list[i].get('name'))
    print("Weigth : ",list[i].get('weigth'))
    wg = float(list[i].get('weigth')) #conversion of string to float 
    print("Price : ",list[i].get('price'))
    pr = float(list[i].get('price'))  #conversion of string to float
    bill = wg * pr
    print("Bill is : ",bill) # calculating bill by using converted values 
    #creating a dictonary for creating new object with the bill
    dict = {"name" : list[i].get('name'),"weigth":list[i].get('weigth'),"price":list[i].get('price'),"bill":bill}
    list_cal.append(dict)#Adding it into the new list

#Opening a new json file for printing new json object with its bill
with open('Data_Cal.json','w') as f :
    json.dump(list_cal,f,indent=2)
#printing new dict-object
print(list_cal)

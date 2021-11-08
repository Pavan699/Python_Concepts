'''
@Author: Pavan Nakate
@Date: 2021-11-06 08:10
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-11-06 09:15
@Title : AddressBook 
'''
import csv
import re

class Contacts:
    """
    Description:
        Class having functions to add,print,edit,delete the contacts 
    """
    address_contact = []

    def print_contact():
        """
        Description:
            Function to print the data from csv file
        Parameter:
            None
        Return:
            None
        """
        with open('Contact.csv','r') as read_csv:
            csv_reader = csv.reader(read_csv)

            for contact in csv_reader:
                print(contact)

    def add_contact():
        """
        Description:
            Function to Add contact if it is valid
        Parameter:
            None
        Return:
            None
        """
        first_Name = input("Enter First Name : ")
        def check_fname(firstName):
            """
            Description:
                Function to check the first name
            Parameter:
                first name
            Return:
                True
            """
            if re.match("^[A-Z]{1}[a-z]{2,}$", firstName):
                return True
            else:
                print("Invalid first name.")
        last_Name = input("Enter Last Name : ")
        def check_lname(lastName):
            """
            Description:
                Function to check the last name
            Parameter:
                last name
            Return:
                True
            """
            if re.match("^[A-Z]{1}[a-z]{2,}$", lastName):
                return True
            else:
                print("Invalid last name.")
        address = input("Enter Address : ")
        def check_address(add):
            """
            Description:
                Function to check the address
            Parameter:
                address
            Return:
                True
            """
            if re.match("^[A-Z]{1}[a-z]{2,}$", add):
                return True
            else:
                print("Invalid Address.")
        city = input("Enter City Name : ")
        def check_city(City):
            """
            Description:
                Function to check the city name
            Parameter:
                city name
            Return:
                True
            """
            if re.match("^[A-Z]{1}[a-z]{2,}$", City):
                return True
            else:
                print("Invalid City name.")
        state = input("Enter State Name : ")
        def check_state(State):
            """
            Description:
                Function to check the state name
            Parameter:
                state name
            Return:
                True
            """
            if re.match("^[A-Z]{1}[a-z]{2,}$", State):
                return True
            else:
                print("Invalid State name.")
        zip = input("Enter Zip Code : ")
        def check_zip(Zip):
            """
            Description:
                Function to check the zip code
            Parameter:
                zip code
            Return:
                True
            """
            if re.match("^[1-9]{1}[0-9]{5}$", Zip):
                return True
            else:
                print("Invalid Zip Code.")
        phone_No = input("Enter Phone No. : ")
        def check_phone_no(phone):
            """
            Description:
                Function to check the phone no.
            Parameter:
                phoneno.
            Return:
                True
            """
            if re.match("^[+]{0,1}[0-9]{2}" + " " + "[6-9]{1}[0-9]{9}$", phone):
                return True
            else:
                print("Invalid Phone No.")
        email = input("Enter Email ID : ")
        def check_email(Email_Id):
            """
            Description:
                Function to check the email id
            Parameter:
                email id
            Return:
                True
            """
            if re.match("^[a-z]{1}[a-z0-9]+[.]{0,1}[a-z0-9]+[@]+[a-z]+[.][a-z]{2,3}([.][a-z]{2,3}){0,2}", Email_Id):
                return True
            else:
                print("Invalid Email ID.")

        if check_fname(first_Name) and check_lname(last_Name) and check_address(address) and check_city(city) and check_state(state) and check_zip(zip) and check_phone_no(phone_No) and check_email(email):
            address_contact = [ first_Name,last_Name,address,city,state,zip,phone_No,email]
            print(address_contact)
            with open('NewAddContact.csv','w') as read_csv:
                csv_writer = csv.writer(read_csv, lineterminator='\n')
                header = ('first_Name','last_Name','address','city','state','zip','phone_No','email')

                csv_writer.writerow(header)
                csv_writer.writerow(address_contact)

        else:
            print("Invalid Contact.")

    def delete_contact():
        """
        Description:
             Function to delete the name if it is present
        Parameter:
            None
        Return:
            None
        """
        del_name = input("Enter name to delete the contact : ")
        flag = False
        with open('Contact.csv','r') as read_csv:
            csv_file = csv.reader(read_csv)

            for contact in csv_file:
                if contact[0] == del_name:
                    print(f"{del_name} is Removed.")
                    flag =True
                else:
                    print(contact)
        
        if flag == False:
            print("Entred Name is not in the address-book")

    def edit_contact():
        """
        Description:
             Function to delete the name if it is present
        Parameter:
            None
        Return:
            None
        """
        edit_name = input("Enter name to delete the contact : ")
        flag = False
        with open('Contact.csv','r') as read_csv:
            csv_file = csv.reader(read_csv)

            for contact in csv_file:
                if contact[0] == edit_name:
                    first_Name = input("Enter First Name : ")
                    last_Name = input("Enter Last Name : ")
                    address = input("Enter Address : ")
                    contact[0] = first_Name
                    contact[1] = last_Name
                    contact[2] = address
                    print(contact)
                    flag =True                
        
        if flag == False:
            print("Entred Name is not in the address-book")

if __name__ == "__main__":
    Contacts.print_contact()
    Contacts.add_contact()
    Contacts.delete_contact()
    Contacts.edit_contact()


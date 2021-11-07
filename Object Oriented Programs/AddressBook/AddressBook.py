'''
@Author: Pavan Nakate
@Date: 2021-11-06 08:10
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-11-06 09:15
@Title : AddressBook 
'''
import csv
import Validation

class Operations:

    """
    Description:
        Class having functions to add,print,edit,delete the contacts 
    """
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

    def add_details():
        """
        Description:
            This function is to take user input from user for the contact details.
            If the details are valid then the entered details are saved to json file.
        """         

        details = {}

        firstName = Validation.validate_first_name()
        details['first_Name'] = firstName

        lastName = Validation.validate_last_name()
        details['last_Name'] = lastName

        address = Validation.validate_address()
        details['address'] = address 

        city = Validation.validate_city()
        details['city'] = city

        state = Validation.validate_state()
        details['state'] = state

        zip = Validation.validate_zip()
        details['zip'] = zip

        mobileNum = Validation.validate_mobile_number()
        details['phone_No'] = mobileNum

        Email = Validation.validate_email()
        details['email'] = Email

        details.append(details) 
        

if __name__ == "__main__":
    Operations.print_contact()
    Operations.add_details()
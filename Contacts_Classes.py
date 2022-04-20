#!/usr/bin/env python3

# Name: Benjamin M. Boden
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 16/04/12022
# Project #: M10
''' I declare that the source code contained in this assignment was written solely by me.
    I understand that copying any source code, in whole or in part, 
    constitutes cheating, and that I will receive a zero on this project
    if I am found in violation of this policy.'''


import csv # get csv tools


# Class: Contact_Consol
# Purpos: gets and munipulates all the csv data for user
# Perameters: path => the location of the text file
class Contact_Consol():
    PATHNAME:str # text file location

    def __init__(self, path):
        self.PATHNAME = path # sets the path name for the object
    

    # Function: read_file()
    # Purpos: gets the data from the csv file
    # purameters: self => the instanc object
    def read_file(self):
        data = [] # declare variable
        with open(self.PATHNAME, newline="") as file: # opens the csv to RAM
            reader = csv.reader(file) # gets the data
            for row in reader: # for every row in the file
                data.append(row) # save it to a local linked list
        return data # return this list


    # Function: write_file()
    # purpos: saves data to the CSV file
    # Peramaters: contacts => the local linked list to be saved as a CSV
    def write_file(self, contacts):
        with open(self.PATHNAME, "w", newline="") as file: # opens a IO conection to RAM
            writer = csv.writer(file) # gets it usable
            writer.writerows(contacts) # saves linked list to the CSV


    # Function: display()
    # Purpos: prints the linked list line by line to console
    # Peramaters: contacts => the local linke list to be printed
    def display(self, contacts):
        for row in contacts: # for each row in the list
            print(f"{row[0]} - {row[1]} - {row[2]}") # print it
        print() # print a blank line


    # Function: view_yearly_summary()
    # Purpos: calculates a data sumery to print to screen
    # Peramaters: contacts => the local linked list to be summariesd
    def view (self, contacts):
        number = self.get_contact_number(contacts)

        if number == 0:
            contact = contacts[number-1]
            print("Name:", contact[0])
            print("Email:", contact[1])
            print("Phone:", contact[2])
            print() 
        else:
            pass


    def get_contact_number(self, contacts):
        while True:
            try:
                number = int(input("Number: "))
            except ValueError:
                print("Invalid integer.\n")
                return -1
                
            if number < 1 or number > len(contacts):
                print("Invalid contact number.\n")
                return -1
            else:
                return number

    
    def add(self, contacts):
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        contact = []
        contact.append(name)
        contact.append(email)
        contact.append(phone)
        contacts.append(contact)
        self.write_contacts(contacts)

        print (f"{contact[0]} was added.")
        print ()

    
    def delete(self, contacts):
        number = self.get_contact_number(contacts)
        if number > 0:
            contact = contacts.pop(number-1)
            print(f"{contact[0]} was deleted.\n")
        self.write_contacts(contacts)

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
import sys
import Contact_Obj as CO

# Class: Contact_Consol
# Purpos: gets and munipulates all the csv data for user
# Perameters: path => the location of the text file
class Contact_Consol():
    PATHNAME:str # text file location
    contacts:object

    def __init__(self, path):
        self.PATHNAME = path # sets the path name for the object
        self.consol_loop()
        

    
    def consol_loop (self):
        self.contacts = CO.Contacts_Obj(self.PATHNAME)
        
        ###contacts = self.read_file() # get the csv contents

        self.display_title() # print tital
        self.display_menu() # print menu

        while True: # run forever
            command = input("Command: ") # get user input
            if command == "list":
                self.display(self.contacts) # if this comand do that
            elif command == "view":
                self.view(self.contacts)  # if this comand do that
            elif command == "add":
               self.add(self.contacts)# if this comand do that
            elif command == "del":
                self.delete(self.contacts) # if this command do that
            elif command == "exit":
                print("Bye!") # print end message
                sys.exit() # if this comand do that
            else:
                print("Not a valid command. Please try again.\contacts") # or have them try again

    
    # Function: display_title()
    # Description: print the program tital to consol
    # Perameters: None
    def display_title(self):
        print("Benjamin Boden's Contact Database") # Tital
        print() # print new line


    # Function display_menu()
    # Description: prints the comand menu to screen
    # Perameters: None
    def display_menu(self):
        print('''COMMAND MENU

                list - Display all contacts
                view - View a contact
                add - Add a contact
                del - Delete a contact
                exit - Exit program''') # print the menu witht this formating
        print() # new line


    # Function: display()
    # Purpos: prints the linked list line by line to console
    # Peramaters: contacts => the local linke list to be printed
    def display(self, contact_obj):
        contacts = contact_obj.get_CONTACTS()
        print ("Name\t-\tEmail\t-\tPhone") # creat list header
        for row in contacts: # for each row in the list
            print(f"{row[0]}\t-\t{row[1]}\t-\t{row[2]}") # print it
        print() # print a blank line


    # Function: view_yearly_summary()
    # Purpos: calculates a data sumery to print to screen
    # Peramaters: contacts => the local linked list to be summariesd
    def view (self, contact_obj):
        contacts = contact_obj.get_CONTACTS()
        number = self.get_contact_number(contacts)

        if number >= 1:
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

    
    def add(self, contact_obj):
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        contact = []
        contact.append(name)
        contact.append(email)
        contact.append(phone)
        

        print (f"{contact[0]} was added.")
        print ()
        contact_obj.set_CONTACTS(contact)

    
    def delete(self, contact_obj):
        contacts = contact_obj.get_CONTACTS()
        num = self.get_contact_number(contacts) - 1
        print(f"{contacts[num]} was deleted.\n")
        contact_obj.remove_CONTACTS(num)
        
        

#!/usr/bin/env python3

# Name: Benjamin M. Boden
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 22/04/12022
# Project #: M11
''' I declare that the source code contained in this assignment was written solely by me.
    I understand that copying any source code, in whole or in part, 
    constitutes cheating, and that I will receive a zero on this project
    if I am found in violation of this policy.'''



import sys # include dependencies
import Contact_Obj as CO # include dependencies

# Class: Contact_Consol
# Purpos: gets and munipulates all the csv data for user
# Perameters: path => the location of the text file
class Contact_Consol():
    PATHNAME:str # text file location
    contacts:object # file list object

    def __init__(self, path):
        self.PATHNAME = path # sets the path name for the object
        self.consol_loop() # start running main loop
        

    # function: consol_loop()
    # Job: program loop
    # perameters: self => self
    def consol_loop (self):
        self.contacts = CO.Contacts_Obj(self.PATHNAME) # initiat object
        
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
                print("Not a valid command. Please try again.") # or have them try again

    
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


    # Function: view ()
    # Purpos: shows a single contact to be used
    # Peramaters: contacts_obj => the object containing the liked list
    def view (self, contact_obj):
        contacts = contact_obj.get_CONTACTS() # get the objects list
        number = self.get_contact_number(contacts) # get user input

        if number >= 1: # if the number is in range do:
            contact = contacts[number-1] # get the list line from the 2D list
            print("Name:", contact[0]) # print the list
            print("Email:", contact[1]) # print the list
            print("Phone:", contact[2]) # print the list
            print() # print new line
        else: # or do this:
            pass # do nothing

    
    # Function: get_contact_number()
    # Job: Gets a valed number form the user
    # Perameters: self => self, contacts => 2D linked list to be used to validate agians
    def get_contact_number(self, contacts):
        while True: # start infinet loop
            try: # first try this
                number = int(input("Number: ")) # get user input
            except ValueError: # if this error acurs
                print("Invalid integer.\n") # print message
                continue # restart the loop
            
            if number < 1 or number > len(contacts): # since no errors acurd, check if in range of list
                print("Invalid contact number.\n") # tell user its wrong
                continue # restart loop
            else: # or its valed:
                return number # return the valed number

    
    # function: add()
    # Job: adds and entry to the 2D list and saves to CSV file
    # Peramiters: self => self, contact_obj => the object conating the 2D list
    def add(self, contact_obj): 
        name = input("Name: ") # get user input as string
        email = input("Email: ") # get user input as string
        phone = input("Phone: ") # get user input as string

        contact = [] # declare short list
        contact.append(name) # add varaible to list
        contact.append(email) # add variable to list
        contact.append(phone) # add variable to list
         
        print (f"{contact[0]} was added.") # notify user
        print () # print new lin
        contact_obj.set_CONTACTS(contact) # save to master object

    
    # Function: delete()
    # Job: removes a contact from the 2D list
    # peramaters: self => self, contact_obj => the object containg the 2D list
    def delete(self, contact_obj):
        contacts = contact_obj.get_CONTACTS() # gets the 2D list from the object
        
        num = self.get_contact_number(contacts) - 1 # gets valed user input
        print(f"{contacts[num[0]]} was deleted.\n") # print message to user
        
        contact_obj.remove_CONTACTS(num) # removes the contact from the master object
        
        

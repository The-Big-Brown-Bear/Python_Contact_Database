#!/usr/bin/env python3

# Name: Benjamin M. Boden
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 20/04/12022
# Project #: M11
''' I declare that the source code contained in this assignment was written solely by me.
    I understand that copying any source code, in whole or in part, 
    constitutes cheating, and that I will receive a zero on this project
    if I am found in violation of this policy.'''


import Monthly_Sales_class as MS # import my monthly comtacts module

FILENAME = "MO11_Project\contacts.csv" # declare the file path constant


# Function: display_title()
# Description: print the program tital to consol
# Perameters: None
def display_title():
    print("Benjamin Boden's Contact Database") # Tital
    print() # print new line


# Function display_menu()
# Description: prints the comand menu to screen
# Perameters: None
def display_menu():
    print('''COMMAND MENU

            list - Display all contacts
            view - View a contact
            add - Add a contact
            del - Delete a contact
            exit - Exit program''') # print the menu witht this formating
    print() # new line


# Name: main () function
# Description: main program function
# Peramiters: None
def main ():
    comtacts = [] # declare variable

    contact_list = MS.Monthly_Sales(FILENAME) # creat new object

    display_title() # print tital
    display_menu() # print menu
    
    comtacts = contact_list.read_file() # get the csv contents

    while True: # run forever
        command = input("Command: ") # get user input
        if command == "lsit":
         contact_list.view_monthly_sales(comtacts) # if this comand do that
        elif command == "view":
         contact_list.view_yearly_summary(comtacts)  # if this comand do that
        elif command == "add":
         contact_list.edit(comtacts) # if this comand do that
        elif command == "del":
            pass
        elif command == "exit":
            break # if this comand do that
        else:
            print("Not a valid command. Please try again.\n") # or have them try again
    
    print("Bye!") # print end message


# Run main () program function
if __name__ == "__main__" : main ()
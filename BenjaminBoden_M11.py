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


import Monthly_Sales_class as MS # import my monthly sales modul

FILENAME = "MO10_Project\Python-csv-Reader\monthly_sales.csv" # declar the file path constant


# Function: display_title()
# Description: print the program tital to consol
# Perameters: None
def display_title():
    print("Benjamin Boden's Monthly Sales") # Tital
    print() # print new line


# Function display_menu()
# Description: prints the comand menu to screen
# Perameters: None
def display_menu():
    print('''COMMAND MENU

            monthly - View monthly sales
            yearly  - View yearly summary
            edit    - Edit sales for a month
            exit    - Exit program''') # print the menu witht this formating
    print() # new line


# Name: main () function
# Description: main program function
# Peramiters: None
def main ():
    sales = [] # declare variable

    monthly_sales = MS.Monthly_Sales(FILENAME) # creat new object

    display_title() # print tital
    display_menu() # print menu
    
    sales = monthly_sales.read_file() # get the csv contents

    while True: # run forever
        command = input("Command: ") # get user input
        if command == "monthly":
            monthly_sales.view_monthly_sales(sales) # if this comand do that
        elif command == "yearly":
            monthly_sales.view_yearly_summary(sales)  # if this comand do that
        elif command == "edit":
            monthly_sales.edit(sales) # if this comand do that
        elif command == "exit":
            break # if this comand do that
        else:
            print("Not a valid command. Please try again.\n") # or have them try again
    
    print("Bye!") # print end message


# Run main () program function
if __name__ == "__main__" : main ()
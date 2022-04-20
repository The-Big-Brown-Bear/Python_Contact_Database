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
    # Peramaters: sales => the local linked list to be saved as a CSV
    def write_file(self, sales):
        with open(self.PATHNAME, "w", newline="") as file: # opens a IO conection to RAM
            writer = csv.writer(file) # gets it usable
            writer.writerows(sales) # saves linked list to the CSV


    # Function: view_monthly_sales()
    # Purpos: prints the linked list line by line to console
    # Peramaters: sales => the local linke list to be printed
    def view_monthly_sales(self, sales):
        for row in sales: # for each row in the list
            print(f"{row[0]} - {row[1]}") # print it
        print() # print a blaink line


    # Function: view_yearly_summary()
    # Purpos: calculates a data sumery to print to screen
    # Peramaters: sales => the local linked list to be summariesd
    def  view_yearly_summary(self, sales):
        total = 0 # declare varialbe
        for row in sales: # for each row
            amount = int(row[1]) # get the value stored at the end of the row
            total += amount # add to total

        # get count
        count = len(sales)
        
        # calculate average
        average = total / count
        average = round(average, 2) # round that answer

        # format and display the result
        print("Yearly total:    ", total) # result
        print("Monthly average: ", average) # result 
        print() # print new line


    # Function: edit()
    # Purpos: changes one of the months values acording to user input and saves it to the CSV
    # Perameters: sales => the local linke list to be changend
    def edit(self,sales):
        names = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'] # sets the lis of months

        l = "Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec" # creats a long string

        print("Months: "+l) # print that long string

        valid = False # declare variable

        while valid != True: # infinet loop
            name = input("What month?\t") # get user input
            if name.lower() == 'jan': valid = True # right month? break loop
            elif name.lower() == 'feb': valid = True # right month? break loop
            elif name.lower() == 'mar': valid = True # right month? break loop
            elif name.lower() == 'apr': valid = True # right month? break loop
            elif name.lower() == names[4].lower(): valid = True # right month? break loop
            elif name.lower() == names[5].lower(): valid = True # right month? break loop
            elif name.lower() == names[6].lower(): valid = True # right month? break loop
            elif name.lower() == names[7].lower(): valid = True # right month? break loop # right month? break loop
            elif name.lower() == names[8].lower(): valid = True # right month? break loop
            elif name.lower() == names[9].lower(): valid = True # right month? break loop
            elif name.lower() == names[10].lower(): valid = True # right month? break loop
            elif name.lower() == names[11].lower(): valid = True # right month? break loop
            else: # otherwise get user to corect
                print("Invalid three-letter month.") # print line
                print("Pleas print one of these: \n\t"+l) # print line

        index_of = names.index(name.lower()) # locate what month they said

        amount = int(input("Sales Amount: ")) # get user input

        month = [] # declare list

        month.append(name) # add the mothe to end of list
        month.append(str(amount)) # add the user input to end of list
        sales[index_of] = month # save that list to the location of the big list

        self.write_file(sales) # save list to CSV
        print(f"Sales amount for {month[0]} was modified.") # print to consol
        print() # print new line
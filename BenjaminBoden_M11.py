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


FILENAME = "MO11_Project\contacts.csv" # declare the file path constant


# Name: main () function
# Description: main program function
# Peramiters: None
def main ():
    import Contacts_Classes as CC # import my monthly contacts module

    contact_list = CC.Contact_Consol(FILENAME) # creat new object  
    
    


# Run main () program function
if __name__ == "__main__" : main ()
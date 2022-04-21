import csv #import dependencies

class Contacts_Obj ():
    PATHNAME:str # text file location
    CONTACTS:list # content of list

    # function: __init__()
    # job: initiats the object
    # Peramaters: self => object, path => the file location
    def __init__(self, path):
        self.PATHNAME = path # sets the path name for the object
        self.CONTACTS = self.read_file() # gets the file contents


    # Function: get_CONTACTS()
    # Job: returns the objects data
    # Peramaters: self => self
    def get_CONTACTS(self):
        data = self.CONTACTS # set 2D list
        return data # return 2D list

    
    # Function: set_CONTACTS()
    # Job: sets new data to the 2D list
    # Peramaters: self => self, new_contact => new list to be added
    def set_CONTACTS(self,new_contact):
        self.CONTACTS.append(new_contact) # add new list to the big 2D list
        self.write_file(self.CONTACTS) # save data

    
    # Function: remove_CONTACTS ()
    # Job: removes data from list
    # peramaters: self => self, num => the number entry that gets removed
    def remove_CONTACTS (self,num):
        if num >= 0 and num <= len(self.CONTACTS): # if its in range
            contact = self.CONTACTS.pop(num) # remove that entry
            self.write_file(self.CONTACTS) # save to file


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
    
    
    
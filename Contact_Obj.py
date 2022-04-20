import csv

class Contacts_Obj ():
    PATHNAME:str # text file location
    CONTACTS:list # content of list


    def __init__(self, path):
        self.PATHNAME = path # sets the path name for the object
        self.CONTACTS = self.read_file()


    def get_CONTACTS(self):
        data = self.CONTACTS
        return data

    
    def set_CONTACTS(self,new_contact):
        self.CONTACTS.append(new_contact)
        self.write_file(self.CONTACTS)


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
    
    
    
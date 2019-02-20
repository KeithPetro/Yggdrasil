from gedcom import Gedcom
import os

def getGedcom(path):
    
    outstring = "-----------\nGEDCOM Test Output\n-----------\n"
    
    #Iterate over all files in the sample-gedcom folder
    for gedcom_filename in os.listdir(path):
        print(gedcom_filename)
        file_path = path + gedcom_filename
        #Create Gedcom instance at path file_path and with strict parsing off
        gedcom = Gedcom(file_path, False)
        #Get all records in the tree
        all_records = gedcom.get_root_child_elements()
    
        #Print name of GEDCOM file being read
        outstring += "-----------\n" + gedcom_filename + "\n-----------\n"
    
        for record in all_records:
            #Check if the record is of a person
            if record.is_individual():
                (first, last) = record.get_name()
                outstring += first + " " + last + "\n"
    return outstring
from gedcom import Gedcom
import os

#Iterate over all files in the sample-gedcom folder
for gedcom_filename in os.listdir("./sample-gedcom/"):
    
    file_path = './sample-gedcom/' + gedcom_filename
    #Create Gedcom instance at path file_path and with strict parsing off
    gedcom = Gedcom(file_path, False)
    #Get all records in the tree
    all_records = gedcom.get_root_child_elements()
    
    #Print name of GEDCOM file being read
    print("\n-----------\n" + gedcom_filename + "\n-----------")
    
    for record in all_records:
        #Check if the record is of a person
        if record.is_individual():
            (first, last) = record.get_name()
            print(first + " " + last)
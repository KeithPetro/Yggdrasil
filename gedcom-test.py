from gedcom import Gedcom

file_path = './sample-gedcom/PAFCHILONLY.GED'
#Create Gedcom instance at path file_path and with strict parsing off
gedcom = Gedcom(file_path, False)
#Get all records in the tree
all_records = gedcom.get_root_child_elements()

for record in all_records:
    #Check if the record is of a person
    if record.is_individual():
        (first, last) = record.get_name()
        print(first + " " + last)
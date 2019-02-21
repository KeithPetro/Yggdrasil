from gedcom import Gedcom
from mainapp.models import Family, Element
import os

def getGedcom(path):
    
    #Iterate over all files in the sample-gedcom folder
    for gedcom_filename in os.listdir(path):
        file_path = path + gedcom_filename
        #Create Gedcom instance at path file_path and with strict parsing off
        gedcom = Gedcom(file_path, False)
        
        gedcom_tree = Family.objects.get_or_create(args=gedcom)#name=gedcom.name, root_element=Element.objects.get_or_create(gedcom.root_element))
        # gedcom_tree.args = gedcom
        # gedcom_tree.save()
        
        # #Get all records in the tree
        # all_records = gedcom.get_root_child_elements()
    
        # for record in all_records:
        #     gedcom_tree.root_element
            
        # gedcom_tree.save()
            
    # return gedcom_tree
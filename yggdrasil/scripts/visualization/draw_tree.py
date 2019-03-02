from gedcom import *
from django.conf import settings
import os

def drawTree():
    for gedcom_file in os.listdir(settings.GEDCOM_DIR):
        gedcom = Gedcom(settings.GEDCOM_DIR + gedcom_file, False)
        
        all_records = gedcom.get_root_child_elements();
        
        for record in all_records:
            if record.get_tag() == "INDI":
                first_person = record
                break
            
        print(first_person.get_name())
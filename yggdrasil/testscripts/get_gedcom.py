from gedcom import *
from mainapp.models import Family, Individual
import json
import datetime
import os

def getGedcom(path):
    
    #Iterate over all files in the sample-gedcom folder
    for gedcom_filename in os.listdir(path):
        file_path = path + gedcom_filename
        #Create Gedcom instance at path file_path and with strict parsing off
        gedcom = Gedcom(file_path, False)
        
        
        # gedcom_tree.args = gedcom
        # gedcom_tree.save()
        
        #Get all records in the tree
        all_records = gedcom.get_root_child_elements()
    
        for record in all_records:
            if record.get_tag() == "FAM":
                family_members_gedcom = gedcom.get_family_members(record, "ALL")
                children_model = []
                parents_model = []
                
                (family, created) = Family.objects.get_or_create()
                
                for member in family_members_gedcom:
                    (element, created) = Individual.objects.get_or_create(  firstname = member.get_name()[0],
                                                                            lastname = member.get_name()[1],
                                                                            gender = member.get_gender(),
                                                                            occupation = member.get_occupation(),
                                                                            is_child = member.is_child(),
                                                                            is_deceased = member.is_deceased(),
                                                                            birth_date = member.get_birth_data()[0],
                                                                            birth_place = member.get_birth_data()[1],
                                                                            death_date = member.get_death_data()[0],
                                                                            death_place = member.get_death_data()[1],
                                                                            burial_date = member.get_burial()[0],
                                                                            burial_place = member.get_burial()[1],
                                                                            last_change_date = datetime.date.today(),
                                                                            marriage_data = json.dumps(gedcom.get_marriages(member))
                                                                        )
                    
                    family.members.add(element)
                    
                    if member.is_child == True:
                        children_model.append(element)
                    else:
                        parents_model.append(element)
                    
                for child in children_model:
                    for parent in parents_model:
                        child.parents.add(parent)
                
                for parent in parents_model:
                    for child in children_model:
                        parent.parents.add(child)
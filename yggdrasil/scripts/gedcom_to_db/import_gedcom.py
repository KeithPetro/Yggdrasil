from gedcom import *
from mainapp.models import *
import json
import datetime
import os

def importGedcom(path):
    #Iterate over all files in the sample-gedcom folder
    for gedcom_filename in os.listdir(path):
        file_path = path + gedcom_filename
        #Create Gedcom instance at path file_path and with strict parsing off
        gedcom = Gedcom(file_path, False)
        
        #Get all records in the tree
        all_records = gedcom.get_root_child_elements()
    
        for record in all_records:
            if record.get_tag() == "FAM":
                family_members_gedcom_p = gedcom.get_family_members(record, "PARENTS")

                family_members_gedcom_c = gedcom.get_family_members(record, "CHIL")

                parents_model = []
                children_model = []
                
                (family, created) = Family.objects.get_or_create(pointer=record.get_pointer())
                
                for parent in family_members_gedcom_p:
                    (element, created) = Individual.objects.get_or_create(  firstname = parent.get_name()[0],
                                                                            lastname = parent.get_name()[1],
                                                                            gender = parent.get_gender(),
                                                                            occupation = parent.get_occupation(),
                                                                            is_child = parent.is_child(),
                                                                            is_deceased = parent.is_deceased(),
                                                                            birth_date = parent.get_birth_data()[0],
                                                                            birth_place = parent.get_birth_data()[1],
                                                                            death_date = parent.get_death_data()[0],
                                                                            death_place = parent.get_death_data()[1],
                                                                            burial_date = parent.get_burial()[0],
                                                                            burial_place = parent.get_burial()[1],
                                                                            last_change_date = datetime.date.today(),
                                                                            marriage_data = json.dumps(gedcom.get_marriages(parent)),
                                                                        )
                                                                        
                    family.members.add(element)
                    element.family.add(family)
                    parents_model.append(element)
                
                for child in family_members_gedcom_c:
                    (element, created) = Individual.objects.get_or_create(  firstname = child.get_name()[0],
                                                                            lastname = child.get_name()[1],
                                                                            gender = child.get_gender(),
                                                                            occupation = child.get_occupation(),
                                                                            is_child = child.is_child(),
                                                                            is_deceased = child.is_deceased(),
                                                                            birth_date = child.get_birth_data()[0],
                                                                            birth_place = child.get_birth_data()[1],
                                                                            death_date = child.get_death_data()[0],
                                                                            death_place = child.get_death_data()[1],
                                                                            burial_date = child.get_burial()[0],
                                                                            burial_place = child.get_burial()[1],
                                                                            last_change_date = datetime.date.today(),
                                                                            marriage_data = json.dumps(gedcom.get_marriages(child)),
                                                                        )
                                                                        
                    family.members.add(element)
                    element.family.add(family)
                    children_model.append(element)
                
                
                for child in children_model:
                    for parent in parents_model:
                        (element, created) = Relation.objects.get_or_create(    parent = parent,
                                                                                child = child
                                                                            )
                        child.relations.add(element)
                        parent.relations.add(element)
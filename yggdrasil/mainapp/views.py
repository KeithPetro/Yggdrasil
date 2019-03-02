from django.shortcuts import render
from django.http import HttpResponse
from scripts.gedcom_to_db.import_gedcom import importGedcom
from mainapp.models import Family, Individual
from django.conf import settings
import os

def gedcom_test_page(request):
    #------------------------------------------------
    #TODO: Clean up this code when the model stucture is finalized
    #------------------------------------------------
    
    importGedcom(settings.GEDCOM_DIR)
    individuals = Individual.objects.all()
    
    individual_names = []
    
    for individual in individuals:
        firstname = individual.firstname
        lastname = individual.lastname
        individual_names.append(firstname + " " + lastname)
        
    return render(request, 'gedcom_test_page.html', {'individual_names': individual_names})
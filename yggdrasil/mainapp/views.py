from django.shortcuts import render
from django.http import HttpResponse
from testscripts.get_gedcom import getGedcom
from mainapp.models import Family, Individual
import os

def gedcom_test_page(request):
    #------------------------------------------------
    #TODO: Clean up this code when the model stucture is finalized
    #------------------------------------------------
    
    getGedcom("./samplegedcom/")
    individuals = Individual.objects.all()
    individual_names = []
    
    for individual in individuals:
        firstname = individual.firstname
        lastname = individual.lastname
        individual_names.append(firstname + " " + lastname)
        
    return render(request, 'gedcom_test_page.html', {'individual_names': individual_names})
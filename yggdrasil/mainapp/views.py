from django.shortcuts import render
from django.http import HttpResponse
from testscripts.get_gedcom import getGedcom
from mainapp.models import Family, Element
import os

def gedcom_test_page(request):
    #------------------------------------------------
    #TODO: Clean up this code when the model stucture is finalized
    #------------------------------------------------
    
    getGedcom("./samplegedcom/")
    families = Family.objects.all()
    individuals = []
    for family in families:
        for individual in family.args.get_root_child_elements():
            if individual.is_individual():
                (first, last) = individual.get_name()
                print(first)
                individuals.append(first + " " + last)
    print(individuals)
    return render(request, 'gedcom_test_page.html', {'individuals': individuals})
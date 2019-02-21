from django.shortcuts import render
from django.http import HttpResponse
from testscripts.get_gedcom import getGedcom
import os

def gedcom_test_page(request):
    test_gedcom = getGedcom("./samplegedcom/").replace("\n", "<br>")
    return render(request, 'gedcom_test_page.html', {'test_gedcom': test_gedcom})
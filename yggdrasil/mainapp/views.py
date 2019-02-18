from django.shortcuts import render
from django.http import HttpResponse
from testscripts.get_gedcom import getGedcom
import os

def home(request):
    return HttpResponse(getGedcom("./samplegedcom/"))
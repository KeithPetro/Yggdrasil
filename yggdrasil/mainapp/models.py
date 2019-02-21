from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
#------------------------------------------------
#TODO: Clean up and finalize this model structure
#------------------------------------------------

class Element(models.Model):
    #Local field(s):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    occupation = models.CharField(max_length=25)
    is_individual = models.IntegerField()
    is_child = models.IntegerField()
    is_family = models.IntegerField()
    is_deceased = models.IntegerField()
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=25)
    death_date = models.DateField()
    death_place = models.CharField(max_length=25)
    burial_date = models.DateField()
    burial_place = models.CharField(max_length=25)
    last_change_date = models.DateField()
    marriage_date = models.DateField()
    
    #One-to-many field(s):
    spouse = models.ForeignKey("self", on_delete=models.CASCADE)
    
    #Many-to-many field(s):
    parents = models.ManyToManyField("self")
    children = models.ManyToManyField("self")

class Family(models.Model):
    
    # #Local field(s):
    # name = models.CharField(max_length=25)
    
    # #One-to-one field(s):
    # root_element = models.OneToOneField(Element, on_delete=models.CASCADE, primary_key=True)
    args = PickledObjectField()
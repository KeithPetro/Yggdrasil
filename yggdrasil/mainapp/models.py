from django.db import models
from django.contrib.auth.models import User

class Individual(models.Model):
    #Local field(s):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    occupation = models.CharField(max_length=25)
    is_child = models.BooleanField()
    is_deceased = models.BooleanField()
    birth_date = models.CharField(max_length=50)
    birth_place = models.CharField(max_length=50)
    death_date = models.CharField(max_length=50)
    death_place = models.CharField(max_length=50)
    burial_date = models.CharField(max_length=50)
    burial_place = models.CharField(max_length=50)
    last_change_date = models.DateField()
    marriage_data = models.CharField(max_length=50)
    
    #Many-to-many field(s):
    relations = models.ManyToManyField("Relation")
    
class Relation(models.Model):
    parent = models.ForeignKey(Individual, on_delete=models.CASCADE, related_name = "parent_accessor")
    child = models.ForeignKey(Individual, on_delete=models.CASCADE,  related_name = "child_accessor")

class Family(models.Model):
    
    #Local fields:
    pointer = models.CharField(max_length=25)
    #Many-to-many field(s):
    members = models.ManyToManyField(Individual, related_name = 'family')
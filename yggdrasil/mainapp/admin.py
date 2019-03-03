from django.contrib import admin
from .models import *

admin.site.site_header = "Yggdrasil Admin"

class IndividualAdmin(admin.ModelAdmin):
    list_display = ('individual','firstname', 'lastname', 'gender', 'last_change_date')
    
    def individual(self,obj):
        return obj.firstname + " " + obj.lastname
    
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Family)
admin.site.register(Relation)
'''Écrit par ROUSSEL Damien, MEDHAOUI Abdelamine, DIALLO Abdoul, DAOUDI Yassir et EL GUERCH Souhail'''

from django.contrib import admin
from .models import *

class FormeMotAdmin(admin.ModelAdmin):
    model = FormeMot
    list_display = ('Affiche','Infos')
    ordering = ('Affiche',)
    search_fields = ('Affiche','Infos')

class TableTransformationAdmin(admin.ModelAdmin):
    model = TableTransformation
    list_display = ('NumTab','Terminaison','Transformation','Infos')
    list_filter = ('NumTab',)
    ordering = ('NumTab',)
    search_fields = ('NumTab','Terminaison','Transformation','Infos')

class MotAdmin(admin.ModelAdmin):
    model = Mot
    list_display = ('Affiche','Table','Cat','Infos')
    list_filter = ('Table','Cat')
    ordering = ('Affiche','Cat','Table')
    search_fields = ('Affiche','Table','Cat','Infos')

admin.site.register(FormeMot,FormeMotAdmin)
admin.site.register(TableTransformation,TableTransformationAdmin)
admin.site.register(Mot,MotAdmin)

from django.contrib import admin
from .models import *

class FormeMotAdmin(admin.ModelAdmin):
    model = FormeMot
    list_display = ('Mot','Infos')
    list_filter = ('Mot','Infos')
    ordering = ('Mot',)
    search_fields = ('Mot','Infos')

class TableTransformationAdmin(admin.ModelAdmin):
    model = TableTransformation
    list_display = ('NumTab','Terminaison','Transformation','Infos')
    list_filter = ('NumTab','Terminaison','Transformation','Infos')
    ordering = ('NumTab',)
    search_fields = ('NumTab','Terminaison','Transformation','Infos')

class MotAdmin(admin.ModelAdmin):
    model = Mot
    list_display = ('Mot','Table','Infos')
    list_filter = ('Mot','Table','Infos')
    ordering = ('Mot','Table')
    search_fields = ('Mot','Table','Infos')

class UtilisateurAdmin(admin.ModelAdmin):
    model = Utilisateur
    list_display = ('Nom','Prenom','get_Droit')
    list_filter = ('Nom','Prenom')
    ordering = ('Nom','Prenom','Droit')
    search_fields = ('Nom','Prenom')

    def get_Droit(self,obj):
        switcher={
            0:"Utilisateur",
            1:"Contributeur",
            2:"Administrateur"
        }
        return switcher.get(obj.Droit)
    get_Droit.short_description='Droit'

admin.site.register(FormeMot,FormeMotAdmin)
admin.site.register(TableTransformation,TableTransformationAdmin)
admin.site.register(Mot,MotAdmin)
admin.site.register(Utilisateur,UtilisateurAdmin)

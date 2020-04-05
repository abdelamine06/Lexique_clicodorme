'''Écrit par ROUSSEL Damien, MEDHAOUI Abdelamine, DIALLO Abdoul, DAOUDI Yassir et EL GUERCH Souhail'''

from django import forms
from .models import Mot


class MotForm(forms.ModelForm):

    class Meta:
        model = Mot
        fields = ('Mot','Infos')
        labels = {
            'Mot':'Mot',
            'Infos':'Infos_sur_le_mot'
        }

    def __init__(self, *args, **kwargs):
        super(MotForm,self).__init__(*args, **kwargs)
        self.fields['Mot'].required = True
        self.fields['Infos'].required = True

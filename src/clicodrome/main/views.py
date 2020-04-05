'''Écrit par ROUSSEL Damien, MEDHAOUI Abdelamine, DIALLO Abdoul, DAOUDI Yassir et EL GUERCH Souhail'''

from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from main.models import *
from main.langue import *
from main.export import *
from django.views.generic.edit import  UpdateView
from .forms import MotForm

def home(request):
    #transformeTous()
    is_user=request.user.is_authenticated
    return render(request,"main/home.html",locals())

def tmp(request):
    request.session['recherche']={'v':request.GET.get('v'),
                                'n':request.GET.get('n'),
                                'adj':request.GET.get('adj'),
                                'adv':request.GET.get('adv'),
                                'exp':request.GET.get('exp'),
                                'degre1':request.GET.get('degre1'),
                                'degre2':request.GET.get('degre2'),
                                'degre3':request.GET.get('degre3')}
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    try:
        mot=Mot.objects.get(Mot=recherche)
    except Mot.DoesNotExist:
        try:
            mot=FormeMot.objects.get(Mot=recherche)
        except FormeMot.DoesNotExist:
            return redirect('../')
    res=[]
    dict={'lemmes':{}}
    recherche=request.session['recherche']
    if recherche['v']:
        res+=Mot.objects.filter(Cat='v')
    if recherche['n']:
        res+=Mot.objects.filter(Cat='nc')
    if recherche['adj']:
        res+=Mot.objects.filter(Cat='adj')
    if recherche['adv']:
        res+=Mot.objects.filter(Cat='adv')
    if recherche['exp']:
        res+=Mot.objects.filter(Cat='exp')
    if recherche['degre1']:
        dict['lemmes']['lemme1']=strToDict(mot.Infos)['lemmes']['lemme1']
    if recherche['degre2']:
        dict['lemmes']['lemme2']=strToDict(mot.Infos)['lemmes']['lemme2']
    if recherche['degre3']:
        dict['lemmes']['lemme3']=strToDict(mot.Infos)['lemmes']['lemme3']
    affiche=[]
    resultat=[]
    for r in res:
        if unifiable(strToDict(r.Infos),dict):
            transformations=TableTransformation.objects.filter(NumTab=r.Table)
            formes=[]
            for transformation in transformations:
                formes+=[transforme(r,transformation)]
            affiche+=[[r]+[formes]]
            resultat+=[r.Mot]
    request.session['resultat']=resultat
    is_user=request.user.is_authenticated
    return render(request,"main/recherche.html",locals())

def exportResultat(request):
    resultats=request.session['resultat']
    mots=[]
    for resultat in resultats:
        mots+=[Mot.objects.get(Mot=resultat)]
    exportMots(mots)
    return redirect('/')

def exportFichier(request):
    exportTousMots()
    return redirect('/')

def importFichier(request):
    importMots("lefff.txt")
    return redirect('/')

def mot_list(request):
    context =  Mot.objects.all()
    return render(request, "main/list_mot.html",{'mot_list':context})

def mot_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MotForm()
        else:
            mot = Mot.objects.get(pk=id)
            form = MotForm(instance=mot)
        return render(request, "main/edit_mot.html", {'form': form})
    else:
        if id == 0:
            form = MotForm(request.POST)
        else:
            mot = Mot.objects.get(pk=id)
            form = MotForm(request.POST,instance= mot)
        if form.is_valid():
            form.save()
        return redirect('/List_mots')

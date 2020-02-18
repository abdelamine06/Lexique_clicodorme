from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from main.models import *
from main.langue import *
from main.export import *

def home(request):
    transformeTous()
    return render(request,"main/home.html",locals())

def tmp(request):
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    try:
        mot=Mot.objects.get(Mot=recherche)
    except Mot.DoesNotExist:
        try:
            mot=FormeMot.objects.get(Mot=recherche)
        except FormeMot.DoesNotExist:
            return redirect('../')
    res=Mot.objects.all()
    dict={}
    dict['lemme2']=strToDict(mot.Infos)['lemme2']
    affiche=[]
    resultat=[]
    for r in res:
        test=unification(strToDict(r.Infos),dict)
        if test!={}:
            transformations=TableTransformation.objects.filter(NumTab=r.Table)
            formes=[]
            for transformation in transformations:
                formes+=[transforme(r,transformation)]
            affiche+=[[r]+[formes]]
            resultat+=[r.Mot]
    request.session['resultat']=resultat
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

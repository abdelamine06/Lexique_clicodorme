from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from main.models import *
from main.langue import *

def home(request):
    transformeTous()
    return render(request,"main/home.html",locals())

def tmp(request):
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    mot=Mot.objects.get(Mot=recherche)
    print(mot)
    if mot==None:
        mot=FormeMot.objects.get(Mot=recherche)
    res=Mot.objects.all()
    dict={}
    dict['lemme2']=dictionnaire(mot.Infos)['lemme2']
    transformations=TableTransformation.objects.filter(NumTab=mot.Table)
    affiche=[]
    for r in res:
        test=unification(dictionnaire(r.Infos),dict)
        if test!={}:
            affiche+=[r]
    for aff in affiche:
        for transformation in transformations:
            print(aff.Mot,'->',transforme(aff,transformation).Mot)
    return render(request,"main/recherche.html",locals())

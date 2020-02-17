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
    try:
        mot=Mot.objects.get(Mot=recherche)
    except Mot.DoesNotExist:
        mot=FormeMot.objects.get(Mot=recherche)
    res=Mot.objects.all()
    dict={}
    dict['lemme2']=strToDict(mot.Infos)['lemme2']
    affiche=[]
    for r in res:
        test=unification(strToDict(r.Infos),dict)
        if test!={}:
            transformations=TableTransformation.objects.filter(NumTab=r.Table)
            formes=[]
            for transformation in transformations:
                formes+=[transforme(r,transformation)]
            affiche+=[[r]+[formes]]
    return render(request,"main/recherche.html",locals())

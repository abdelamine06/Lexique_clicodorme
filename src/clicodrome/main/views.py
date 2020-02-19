from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
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

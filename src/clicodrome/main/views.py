from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from main.models import *
import regex

def dictionnaire(mot):
    dict={}
    patternSimple='[^=,\[\]]+=[^,\[\]]+'
    patternComplexe='[^=,\[\]]+=\[((?:[^\[\]]*|(?R))*)\]'
    infos=[]
    tmp=regex.search(patternComplexe,mot)
    if tmp!=None:
        infos+=[tmp.group(0)]
    tmp=regex.sub(patternComplexe,'',mot)
    tmp=regex.findall(patternSimple,tmp)
    if tmp!=[]:
        infos+=tmp
    for info in infos:
        index=info.find('=')
        if '[' in info:
            dict[info[0:index]]=dictionnaire(info[index+2:len(info)-1])
        else:
            dict[info[0:index]]=info[index+1:]
    return dict

def saveDictionnaire(dict):
    res=str(dict)
    res=res[1:len(res)-1]
    res=res.replace('{','[')
    res=res.replace('}',']')
    res=res.replace(':','=')
    return res

def unification(dict1,dict2):
    res=dict1
    for cle,val in dict2.items():
        if cle in dict1:
            if dict1[cle]!=val:
                return {}
        else:
            res[cle]=val
    return res

def transforme(mot,transformation):
    print(transformation.Terminaison)
    terminaisonIndex=mot.Mot.rfind(transformation.Terminaison)
    if transformation.Terminaison=='':
        terminaisonIndex+=1
    formeMot=mot.Mot[:terminaisonIndex+1]+transformation.Transformation
    infos=unification(dictionnaire(mot.Infos),dictionnaire(transformation.Infos))
    if infos!={}:
        formeMot=FormeMot(Mot=formeMot,Infos=saveDictionnaire(infos))
    return formeMot

def transformeTous():
    formesMots=FormeMot.objects.all()
    for formeMot in formesMots:
        formeMot.delete()
    mots=Mot.objects.all()
    for mot in mots:
        transformations=TableTransformation.objects.filter(NumTab=mot.Table)
        for transformation in transformations:
            formeMot=transforme(mot,transformation)
            formeMot.save()

def home(request):
    transformeTous()
    return render(request,"main/home.html",locals())

def tmp(request):
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    mot=Mot.objects.get(Mot=recherche)
    if mot==None:
        mot=FormeMot.objects.get(Mot=recherche)
    res=Mot.objects.all()
    dict={}
    dict['lemme3']=dictionnaire(mot.Infos)['lemme3']
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

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

def unification(dict1,dict2):
    res=dict1
    print(dict1)
    print(dict2)
    for cle,val in dict2.items():
        if cle in dict1:
            print(cle,val,dict1[cle])
            if dict1[cle]!=val:
                return {}
        else:
            res[cle]=val
    return res

def home(request):
    return render(request,"main/home.html",locals())

def tmp(request):
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    mot=Mot.objects.get(Mot=recherche)
    res=Mot.objects.all()
    affiche=[]
    dict={}
    dict['lemme2']='fruit'
    for r in res:
        test=unification(dictionnaire(r.Infos),dict)
        print(test)
        print(r.Mot)
        if test!={}:
            affiche+=[r]
    for aff in affiche:
        print(aff.Mot)
    return render(request,"main/recherche.html",locals())

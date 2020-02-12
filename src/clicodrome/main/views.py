from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from main.models import *
import regex

def home(request):
    return render(request,"main/home.html",locals())

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
    print(infos)
    for info in infos:
        print(info)
        index=info.find('=')
        if '[' in info:
            print('ok')
            dict[info[0:index]]=dictionnaire(info[index+2:len(info)-1])
        else:
            dict[info[0:index]]=info[index+1:]
    return dict

def tmp(request):
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    mot=Mot.objects.get(Mot=recherche)
    infos=dictionnaire(mot.Infos)
    print(infos)
    return redirect('../')

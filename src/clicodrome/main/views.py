from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from main.models import *

def home(request):
    return render(request,"main/home.html",locals())

def dictionnaire(infos):
    dict={}
    infos=infos.split(',')
    for info in infos:
        element=info.split('=')
        if element[1][0]=='[':
            dict[element[0]]=dictionnaire(element[1][1:len(element)-2])
        else:
            dict[element[0]]=element[1]
    return dict


def tmp(request):
    return redirect('/recherche/'+request.GET.get("recherche"))

def recherche(request,recherche):
    mot=Mot.objects.get(Mot=recherche)
    infos=dictionnaire(mot.Infos)
    return redirect('../')

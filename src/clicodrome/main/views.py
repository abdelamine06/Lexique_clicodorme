from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
#from main.models import *
#from main.form import *
#from main.render import Render

def home(request):
    return redirect('/admin')

from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404

def inscription(request):
    if request.method=='POST':
        username=request.POST.get('username')
        prenom=request.POST.get('prenom')
        nom=request.POST.get('nom')
        mail=request.POST.get('mail')
        password=request.POST.get('password')
        if password!=request.POST.get('password2'):
            errorInscription=True
        else:
            user=User.objects.create_user(username,mail,password)
            user.first_name=prenom
            user.last_name=nom
            user.groups.add(Group.objects.get(name='Utilisateur'))
            user.save()
            login(request,user)
            return redirect(request.GET.get('next','../'))
    return render(request,'main/connection.html',locals())


def connexion(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get('next','../'))
        else:
            error=True
    return render(request,'main/connexion.html',locals())

def deconnexion(request):
    logout(request)
    return redirect(request.GET.get('next','../'))

@login_required(redirect_field_name='next',login_url='/connexion')
def editProfile(request):
    if request.method=='POST':
        username=request.POST.get('username')
        prenom=request.POST.get('prenom')
        nom=request.POST.get('nom')
        mail=request.POST.get('mail')
        password=request.POST.get('password')
        user = User.objects.get(username = request.user.username)
        if check_password(password,user.password)==False:
            if password!=request.POST.get('password2'):
                error=True
                return render(request,'main/editProfile.html',locals())
            user.set_password(password)
        user.username=username
        user.first_name=prenom
        user.last_name=nom
        user.email=mail
        user.save()
    is_user=True
    return render(request,'main/editProfile.html',locals())

@login_required(redirect_field_name='next',login_url='/connexion')
def deleteProfile(request):
    user.delete()
    logout(user)
    return redirect(request.GET.get('next','../'))

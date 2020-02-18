"""clicodrome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('recherche',views.tmp),
    path('recherche/<str:recherche>',views.recherche),
    path('exportResultat',views.exportResultat),
    path('export',views.exportFichier),
    path('import',views.importFichier),
    path('List_mots',views.mot_list),
    path('edit_mots/<int:id>/',views.mot_form),

    
]

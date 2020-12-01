"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# Supprimer la ligne : from django.contrib import admin
from django.urls import path

# importer les Views dans laquelle on enverra les requests
from . import views

# Plutard, Quand on voudra créer des urls pour les clients, dynamiquement
app_name = "noyau"
urlpatterns = [
    # Ajouter le path à la quelle les requests de "app_name" sera envoyés
    path("", views.homepage, name="homepage"),
    
    # Supprimer la ligne : path('admin/', admin.site.urls),
]

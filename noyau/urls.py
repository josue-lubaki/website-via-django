# Supprimer la ligne : from django.contrib import admin
from django.urls import path

# importer les Views dans laquelle on enverra les requests
from . import views

# Plutard, Quand on voudra créer des urls pour les clients, dynamiquement
app_name = "noyau"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("logout/", views.logout_request, name="logout"),
    path("connexion/", views.demandeConnexion, name="connexion"),
    path("account/", views.account, name="account"),
]

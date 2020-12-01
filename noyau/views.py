from random import randint
from django.db.models.expressions import Random
from django.shortcuts import render, redirect
from .models import Netfeelex
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import newUser

# Create your views here.

def homepage(request):
    return render(request=request, template_name='main/home.html',
                  context={"netfeelex": Netfeelex.objects.all})


def subscribe(request): 
    if request.method == "POST":
        form = newUser(request.POST)

        if form.is_valid():
            # on créer utilisateur
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"nouveau compte créé: {username}")
            login(request, user)
            messages.info(request, f"vous êtes maintenant connecté en tant que {username}")
            return redirect("noyau:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
                return render(request, "main/subscribe.html", {"formulaire": form})

    form = newUser
    return render(request, "main/subscribe.html", {"formulaire": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Session est fermée")
    return redirect("noyau:homepage")


def demandeConnexion(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)

        if form.is_valid():
            nomUtilisateur = form.cleaned_data.get('username')
            motDePasse = form.cleaned_data.get('password')
            user = authenticate(username = nomUtilisateur, password = motDePasse)

            if user is not None:
                login(request,user)
                messages.info(request, f"Vous êtes maintenant connecté étant que {nomUtilisateur}")
                return redirect("/")
            else:
                messages.error(request, "Nom d'Utilisateur ou Mot de Passe non valide !")
        else:
            messages.error(request, "Nom d'Utilisateur ou Mot de Passe non valide !")

    form = AuthenticationForm()
    return render(request, "main/connexion.html", {"formulaire": form})


def account(request):
    i = randint(0,10)
    motGentil(request,i)
    return redirect("/")


def motGentil(request, argument):
    if argument == 1:
        messages.info(request, "Souriez ♥")
    elif argument == 2:
        messages.info(request, "Je sais, C'est un très beau Prenom")
    elif argument == 3:
        messages.info(request, "Arrête d'avoir envie, Fais-le")
    elif argument == 4:
        messages.info(request, "Mieux vaut ne pas le savoir")
    elif argument == 5:
        messages.info(request, "Tu connais la chanson ♫ Taciturne ♪ de Dinos ?")
    elif argument == 6:
        messages.info(request, "Oui, c'est mon nom, tu doutes ?")
    elif argument == 7:
        messages.info(request, "C'est bientôt Noël ?")
    elif argument == 8:
        messages.info(request, "Le monde est trop petit pour...")
    elif argument == 9:
        messages.info(request, "Tu me ressembles ☺")
    elif argument == 10:
        messages.info(request, "Je te vois ☻")
    else:
        messages.info(request, "Salut, tu vas bien ?")
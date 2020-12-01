from django.shortcuts import render
from django.http import HttpResponse
from .models import Netfeelex
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request=request, template_name='main/home.html',
                  context={"netfeelex": Netfeelex.objects.all})


def subscribe(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # on créer utilisateur
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("noyau:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                return render(request, "main/subscribe.html", {"formulaire": form})

    form = UserCreationForm
    return render(request, "main/subscribe.html", {"formulaire": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Session est fermé")
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


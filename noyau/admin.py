from django.contrib import admin
from .models import Netfeelex
from tinymce.widgets import TinyMCE # importer le Tinymce.widgets
from django.db import models # recuperer les models de la base ded des données
# Register your models here.

    # Pour permuter l'ordre d'affichage de section
class NetfeelexAdmin(admin.ModelAdmin):
    #fields = ["Titre_film", "Date_publication", "Contenu_film"]
    fieldsets = [
        ("Titre/Date",{"fields" : ["Titre_film","Date_publication"]}),
        ("Content", {"fields" : ["Contenu_film"]})
    ]

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()},
    }

admin.site.register(Netfeelex, NetfeelexAdmin)
from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime

# Create your models here.
class Netfeelex(models.Model):
    #CharFiels pour mettre une restriction
    Titre_film = models.CharField(max_length=200)
    Contenu_film = models.TextField()
    Date_publication = models.DateTimeField("Date publié", default = datetime.now())

    #fonction de recuperation
    def __str__(self):
        return self.Titre_film
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class newUser(UserCreationForm):
    courriel = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "courriel",
            "password1",
            "password2"
        )

def save(self, commit=True):
    utilisateur = super(newUser, self).save(commit=False)
    utilisateur.first_name = self.cleaned_data["first_name"]
    utilisateur.last_name = self.cleaned_data["last_name"]
    utilisateur.email = self.cleaned_data["courriel"]
    if commit:
        utilisateur.save()
        return utilisateur


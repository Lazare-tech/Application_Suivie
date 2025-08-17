from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
class LoginForm(forms.Form):
    # Utilisation de l'email pour la connexion
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        max_length=63,
        label="Email",
        error_messages={
            'required': _('Le mail est requis.'),
            'invalid': _('Veuillez entrer une adresse email valide.')
        }
    )

    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Mot de passe',
        error_messages={
            'required': _('Le mot de passe est requis.')
        }
    )
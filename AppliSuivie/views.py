from django.shortcuts import render,redirect
from . import forms
from .forms import  LoginForm
from AppliSuivie.models import User
from django.contrib.auth import login, authenticate,logout
from django.conf import settings

# Create your views here.
def home(request):
    
    return render(request,'AppliSuivie/index.html')
#
def forecast(request):
    return render(request,'AppliSuivie/previsions.html')
#
def alerts(request):
    return render(request,'AppliSuivie/alerts.html')
#
def settings(request):
    return render(request,'AppliSuivie/parametre.html')
#
def transactions(request):
    return render(request,'AppliSuivie/transaction.html')
#
def report(request):
    return render(request,'AppliSuivie/rapport.html')
#


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                print("email:",email)
                # On cherche d'abord un utilisateur ayant cet email
                user = User.objects.get(email=email)
                print("userrr",user)
                # Ensuite, on vérifie que le mot de passe est correct
                user = authenticate(request, username=user.username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('AppliSuivie:dashboard')  # Redirige vers le tableau de bord après connexion
                else:
                    form.add_error(None, 'Identifiants invalides.')
            except User.DoesNotExist:
                form.add_error(None, "Aucun utilisateur n'est enregistré avec cet email.")
    else:
        form = LoginForm()

    return render(request, 'AppliSuivie/login.html', {'form': form})

##################
def logout_user(request):
    logout(request)
    
    return redirect('AppliSuivie:login')
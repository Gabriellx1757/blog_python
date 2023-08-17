from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from perfiles.models import *

class UsuarioForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
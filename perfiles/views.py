from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from perfiles.forms import *
from perfiles.models import *

class ConsultaCreateView(CreateView):
    model = Consulta
    fields = "__all__"
    template_name = "perfiles/consulta_crear.html"
    success_url = reverse_lazy("inicio")

class UsuarioCreateView(CreateView):
    form_class = UsuarioForm
    template_name = "perfiles/registro.html"
    success_url = reverse_lazy("login")

class UsuarioLoginView(LoginView):
    template_name = "perfiles/login.html"
    success_url = reverse_lazy("mi_perfil")

class UsuarioLogoutView(LogoutView):
    template_name = "perfiles/logout.html"

class UsuarioUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = "perfiles/user_form.html"
    success_url = reverse_lazy("mi_perfil")

class UsuarioTemplateView(LoginRequiredMixin, TemplateView):
   template_name = "perfiles/user_detail.html"
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from blog.models import *

class ArticuloListView(ListView):
    model = Articulo
    template_name = "blog/articulo_lista.html"

class ArticuloDetailView(DetailView):
    model = Articulo

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
    success_url = "/articulos/entradas/"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
    success_url = "/articulos/entradas/"

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
   model = Articulo
   success_url = "/articulos/entradas/"

from django.shortcuts import redirect
from django.views import View
from blog.models import Articulo

class VaciarArticulosView(View):
    def get(self, request, *args, **kwargs):
        Articulo.objects.all().delete()  # Elimina todos los artículos
        return redirect("lista_articulos")  # Redirige a la vista de lista de artículos

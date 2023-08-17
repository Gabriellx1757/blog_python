from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

class InicioTemplateView(TemplateView):
    template_name = "inicio.html"

class SobreMiTemplateView(TemplateView):
    template_name = "sobre_mi.html"
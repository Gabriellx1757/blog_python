from django.db import models
from django.contrib.auth.models import User

class Consulta(models.Model):
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    detalle = models.TextField(blank=True)
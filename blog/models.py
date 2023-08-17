from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField(blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to="entradas/", null="True", blank=True)

    def __str__(self):
        return self.titulo     
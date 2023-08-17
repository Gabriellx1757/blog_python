from django.test import TestCase

from django.db import IntegrityError
from blog.models import *
class BlogTest(TestCase):

   def test_creacion_articulo(self):
       articulo = Articulo(titulo="Titulo", subtitulo="Subtitulo", cuerpo="Cuerpo")
       articulo.save()

       self.assertEqual(Articulo.objects.count(), 1)
       self.assertEqual(articulo.titulo, "Titulo")
       self.assertEqual(articulo.subtitulo, "Subtitulo")
       self.assertEqual(articulo.cuerpo, "Cuerpo")
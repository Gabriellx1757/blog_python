from django.contrib import admin
from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("entradas/", ArticuloListView.as_view(), name="lista_articulos"),
    path("entradas/<int:pk>/", ArticuloDetailView.as_view(), name="ver_articulo"),
    path("crear-articulo/", ArticuloCreateView.as_view(), name="crear_articulo"),
    path("editar-articulo/<int:pk>/", ArticuloUpdateView.as_view(), name="editar_articulo"),
    path("vaciar-articulos/", VaciarArticulosView.as_view(), name="vaciar_articulos"),
    path("eliminar-articulo/<int:pk>/", ArticuloDeleteView.as_view(), name="eliminar_articulo"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
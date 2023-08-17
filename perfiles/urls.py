from django.contrib import admin
from django.urls import path
from perfiles.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("contacto/", ConsultaCreateView.as_view(), name="enviar_consulta"),
    path("registro/", UsuarioCreateView.as_view(), name="registro"),
    path("iniciar-sesion/", UsuarioLoginView.as_view(), name="login"),
    path("cerrar-sesion/", UsuarioLogoutView.as_view(), name="logout"),
    path("mi-perfil/", UsuarioTemplateView.as_view(), name="mi_perfil"),
    path("editar-perfil/<int:pk>/", UsuarioUpdateView.as_view(), name="editar_perfil"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
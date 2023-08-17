from django.contrib import admin
from django.urls import path, include
from web_blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", InicioTemplateView.as_view(), name="inicio"),
    path("articulos/", include("blog.urls")),
    path("perfiles/", include("perfiles.urls")),
    path("about/", SobreMiTemplateView.as_view(), name="sobre_mi"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
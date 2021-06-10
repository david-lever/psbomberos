from django.urls import path
from .views import home
from .views import historia
from .views import galeria
from .views import contacto
from .views import bombero


urlpatterns = [
    path('', home, name="home"),
    path('historia', historia, name="historia"),
    path('galeria', galeria, name="galeria"),
    path('contacto', contacto, name="contacto"),
    path('integrantes', bombero, name="bombero"),
]

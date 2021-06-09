from django.urls import path
from .views import home
from .views import historia
from .views import galeria
from .views import nosotros
from .views import contacto
from .views import bombero
from .views import form_personal


urlpatterns = [
    path('', home, name="home"),
    path('historia', historia, name="historia"),
    path('galeria', galeria, name="galeria"),
    path('nosotros', nosotros, name="nosotros"),
    path('contacto', contacto, name="contacto"),
    path('integrantes', bombero, name="bombero"),
    path('integrantes', form_personal, name="bombero"),
]

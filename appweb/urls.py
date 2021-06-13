from django.urls import path
from .views import home
from .views import historia
from .views import galeria
from .views import contacto
from .views import postulante
from .views import editar
from .views import eliminar


urlpatterns = [
    path('', home, name="home"),
    path('historia', historia, name="historia"),
    path('galeria', galeria, name="galeria"),
    path('contacto', contacto, name="contacto"),
    path('postulantes', postulante, name="postulante"),
    path('modificarPostulante/<id>', editar, name="editar"),
    path('eliminarPostulante/<id>', eliminar, name="eliminar"),
]

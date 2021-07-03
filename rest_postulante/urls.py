from django.urls import path
from rest_postulante.views import lista_postulantes, detalle_postulante
from rest_postulante.viewsLogin import login

urlpatterns = [
    path('lista-postulantes', lista_postulantes, name='lista_postulantes'),
    path('detalle-postulante/<id>', detalle_postulante, name='detalle_postulante'),
    path('login', login, name='login'),
]
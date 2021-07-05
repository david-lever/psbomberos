from django.urls import path
from rest_personal.views import lista_personal, detalle_personal
from rest_personal.viewsLogin import login
urlpatterns = [
    path('lista_personal',lista_personal,name='lista_personal'),
    path('detalle-personal/<id>',detalle_personal,name='detalle_personal'),
    path('login',login,name='login'),
]


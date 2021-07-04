from django.urls import path
from rest_personal.views import lista_personal

urlpatterns = [
    path('lista_personal',lista_personal,name='lista_personal'),
]


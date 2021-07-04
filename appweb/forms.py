from django import forms
from django.forms import ModelForm
from .models import Postulante

class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = ['rut', 'pnombre', 'snombre', 'appaterno', 'apmaterno', 'edad','nivel']

from django import forms
from django.forms import ModelForm
from .models import Postulante, Personal

class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = ['rut', 'pnombre', 'snombre', 'appaterno', 'apmaterno', 'edad','nivel']

class PersonalForm():
    class Meta:
        model = Personal
        fields = ['rut', 'dv', 'pnombre', 'snombre', 'appaterno', 'apmaterno','cargo','compania', 'fono','comuna','fecha_ing']

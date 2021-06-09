from django import forms
from django.forms import ModelForm
from .models import Personal

class PersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = ['rut', 'dv', 'pnombre', 'snombre', 'appaterno', 'apmaterno', 'fono', 'fecha_ing', 'cargo', 'compania', 'comuna']
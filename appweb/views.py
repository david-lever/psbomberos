from django.shortcuts import render
from .models import Personal
from .forms import PersonalForm

# Create your views here.

def home(request):
    return render(request, 'appweb/index.html')


def historia(request):
    return render(request, 'appweb/historia.html')


def galeria(request):
    return render(request, 'appweb/galeria.html')


def nosotros(request):
    return render(request, 'appweb/index.html')


def contacto(request):
    return render(request, 'appweb/contacto.html')


def bombero(request):
    listaPersonal = Personal.objects.all()
    datos = {
        'personal':listaPersonal,
    }
    return render(request, 'appweb/personal.html',datos)


def form_personal(request):
    datos = {
        'form':PersonalForm()
    }
    
    return render(request,'appweb/personal.html',datos)
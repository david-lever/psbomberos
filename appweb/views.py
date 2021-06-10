from django.shortcuts import render
from .models import Personal
from .forms import PostulanteForm

#PersonalForm

# Create your views here.

def home(request):
    datos = {
        'form' : PostulanteForm()
    }
    if(request.method == 'POST'):
        formulario = PostulanteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
    return render(request, 'appweb/index.html',datos)

def historia(request):
    return render(request, 'appweb/historia.html')


def galeria(request):
    return render(request, 'appweb/galeria.html')


def contacto(request):
    return render(request, 'appweb/contacto.html')


def bombero(request):
    listaPersonal = Personal.objects.all()
    datos = {
        'personal':listaPersonal
    }
    return render(request, 'appweb/personal.html',datos)
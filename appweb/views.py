from django.shortcuts import render

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

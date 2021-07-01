from django.shortcuts import render, redirect
from .models import Personal, Postulante
from .forms import PostulanteForm, PersonalForm

# Create your views here.

#FORMULARIO DE POSTULANTES
def home(request):
    datos = {
        'form' : PostulanteForm()
    }
    if(request.method == 'POST'):
        formulario = PostulanteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Los Datos de la Postulación se guardaron Correctamente'
        else:
            datos['mensaje'] = 'ERROR. Postulante Ya Registrado en el Sistema.'
    return render(request, 'appweb/index.html',datos)

#MUESTRA LA PAGINA HISTORIA
def historia(request):
    return render(request, 'appweb/historia.html')

#MUESTRA LA PAGINA GALERIA Y LA LISTA DEL PERSONAL
def galeria(request):
    return render(request, 'appweb/galeria.html')


#MUESTRA LA PAGINA CONTACTO
def contacto(request):
    listaPersonal = Personal.objects.all()
    datos = {
        'personal':listaPersonal,
    }
    return render(request, 'appweb/contacto.html',datos)


#MUESTRA LA PAGINA INFORMACIÓN Y LA LISTA DE POSTULANTES
def postulante(request):
    listaPostulantes = Postulante.objects.all()
    datos = {
        'postulante': listaPostulantes,
    }
    return render(request, 'appweb/postulante.html',datos)

#MODIFICAR - ACTUALIZAR
def editar(request, id):
    postulante = Postulante.objects.get(rut=id)
    
    datos = {
        'form': PostulanteForm(instance=postulante)
    }

    if(request.method == 'POST'):
        formulario = PostulanteForm(data=request.POST, instance=postulante)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Los Datos Modificados se Guardaron correctamente'
        
    return render(request,'appweb/modificarpersonal.html',datos)


#ELIMINAR POSTULANTE    
def eliminar(request, id):
    postulante = Postulante.objects.get(rut=id)
    postulante.delete()
    return redirect(to='informacion')

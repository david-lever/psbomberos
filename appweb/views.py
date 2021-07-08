from django.shortcuts import render, redirect
from .models import Personal, Postulante
from .forms import PostulanteForm
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this

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


#MUESTRA LA PAGINA INFORMACION Y LA LISTA DE POSTULANTES
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
            return redirect(to='postulante')
        
    return render(request,'appweb/modificarpersonal.html',datos)


#ELIMINAR POSTULANTE    
def eliminar(request, id):
    postulante = Postulante.objects.get(rut=id)
    postulante.delete()
    return redirect(to='postulante')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("appweb:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="appweb/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("appweb:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="appweb/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("appweb:home")



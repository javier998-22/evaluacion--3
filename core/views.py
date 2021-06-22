from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
# Create your views here.
def home(request):

    return render(request, 'core/home.html')

def home(request):


    libro = Libro.objects.all()

    datos = {
        'libro' : libro 
    }

    return render(request, 'core/home.html', datos)


def form_libro(request):
    datos = {

        'form': LibroForm()

    }
    if request.method== 'POST':

        formulario = LibroForm(request.POST)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = 'Guardados correctamente'

    return render(request, 'core/form_libro.html',datos)


def form_mod_libro(request,id):

    libro = Libro.objects.get(ISBN=id)

    datos={
        'form':LibroForm(instance=libro)

    }
    if request.method=='POST':
        formulario = LibroForm(data=request.POST,instance=vehiculo)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_libro.html', datos)

def form_del_libro(request,id):
    
    libro = Libro.objects.get(ISBN=id)

    vehiculo.delete()

    return redirect(to="home")
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from inicio.models import Mascota, Paleta
from inicio.forms import PaletaFormulario, PaletaFormularioBusqueda


def anio_de_nacimiento(request, edad):
    if not edad.isnumeric():
        return HttpResponse('No se paso por la url un valor correcto. Debe pasar un valor entero.')
        
    anio_actual = datetime.now().year
    anio_de_nacimiento = anio_actual - int(edad)
    return HttpResponse(f'Aproximadamente la persona con {edad} de edad nacio en {anio_de_nacimiento}')

def bienvenida(request):
    return render(request, 'inicio/bienvenida.html')

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_mascota(request, nombre, edad):
    mascota = Mascota(nombre=nombre, edad=edad, fecha=datetime.now())
    mascota.save()
    return render(request, 'inicio/crear_mascota.html', {'mascota': mascota})

def crear_paleta(request):
      if request.method == "POST":
            paleta_formulario = PaletaFormulario(request.POST)
            if paleta_formulario.is_valid():
                informacion = paleta_formulario.cleaned_data
                paleta = Paleta(marca=informacion["marca"], modelo=informacion["modelo"], anio=informacion["anio"], nueva=informacion["nueva"])
                paleta.save()
                
                # v1
                paleta_formulario = PaletaFormulario()
                return render(request, "inicio/crear_paleta.html", {'paleta_formulario': paleta_formulario,'mensaje': 'Se creo correctamente la paleta.'})
                
                # # v2 
                # return redirect('buscar_paleta')
                    
      else:
        paleta_formulario = PaletaFormulario()
      return render(request, "inicio/crear_paleta.html", {"paleta_formulario": paleta_formulario})
  
def buscar_paleta(request):
    modelo = request.GET.get('modelo', '')
    paletas = Paleta.objects.filter(modelo__icontains=modelo)
    paleta_formulario = PaletaFormularioBusqueda()
    return render(request, 'inicio/buscar_paleta.html', {'paleta_formulario': paleta_formulario, 'paletas': paletas, 'modelo': modelo})
    
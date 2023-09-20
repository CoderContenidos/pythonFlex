from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from inicio.models import Mascota


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
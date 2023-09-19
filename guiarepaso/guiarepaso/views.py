from datetime import datetime
from django.http import HttpResponse

def anio_de_nacimiento(request, edad):
    if not edad.isnumeric():
        return HttpResponse('No se paso por la url un valor correcto. Debe pasar un valor entero.')
        
    anio_actual = datetime.now().year
    anio_de_nacimiento = anio_actual - int(edad)
    return HttpResponse(f'Aproximadamente la persona con {edad} de edad nacio en {anio_de_nacimiento}')
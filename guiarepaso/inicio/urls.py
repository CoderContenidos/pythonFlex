from django.urls import path
from inicio.views import anio_de_nacimiento, bienvenida, inicio, crear_mascota, buscar_paleta, crear_paleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida),
    path('edad/<edad>/', anio_de_nacimiento),
    path('crear-mascota/<nombre>/<edad>/', crear_mascota),
    path('paletas/', buscar_paleta, name='buscar_paleta'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
]

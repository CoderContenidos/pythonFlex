from django.urls import path
from inicio.views import anio_de_nacimiento, bienvenida, inicio, crear_mascota

urlpatterns = [
    path('', inicio),
    path('bienvenida/', bienvenida),
    path('edad/<edad>/', anio_de_nacimiento),
    path('crear-mascota/<nombre>/<edad>/', crear_mascota),
]

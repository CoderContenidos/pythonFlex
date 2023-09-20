from django.urls import path
from inicio.views import anio_de_nacimiento, bienvenida, inicio

urlpatterns = [
    path('', inicio),
    path('bienvenida/', bienvenida),
    path('edad/<edad>/', anio_de_nacimiento),
]

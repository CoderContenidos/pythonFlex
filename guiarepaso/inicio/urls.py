from django.urls import path
from inicio.views import anio_de_nacimiento, bienvenida

urlpatterns = [
    path('bienvenida/', bienvenida),
    path('edad/<edad>/', anio_de_nacimiento),
]

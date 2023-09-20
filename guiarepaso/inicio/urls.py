from django.urls import path

# v1
from inicio.views import anio_de_nacimiento, bienvenida, inicio, crear_mascota, buscar_paleta, crear_paleta, editar_paleta, borrar_paleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida),
    path('edad/<edad>/', anio_de_nacimiento),
    path('crear-mascota/<nombre>/<edad>/', crear_mascota),
    path('paletas/', buscar_paleta, name='buscar_paleta'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    path('paletas/editar/<int:paleta_id>/', editar_paleta, name='editar_paleta'),
    path('paletas/borrar/<int:paleta_id>', borrar_paleta, name='borrar_paleta'),
]

# v2 -> ventaja, no armo un lista tan larga de vistas que importo

# from inicio import views

# urlpatterns = [
#     path('', views.inicio, name='inicio'),
#     path('bienvenida/', views.bienvenida),
#     path('edad/<edad>/', views.anio_de_nacimiento),
#     path('crear-mascota/<nombre>/<edad>/', views.crear_mascota),
#     path('paletas/', views.buscar_paleta, name='buscar_paleta'),
#     path('paletas/crear/', views.crear_paleta, name='crear_paleta'),
#     path('paletas/editar/<int:paleta_id>/', views.editar_paleta, name='editar_paleta'),
#     path('paletas/borrar/<int:paleta_id>', views.borrar_paleta, name='borrar_paleta'),
# ]


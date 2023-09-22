from django.urls import path
from peluche import views

urlpatterns = [
    path('animales/', views.PelucheAnimalListView.as_view(), name='listado_peluches_animales'),
    path('animales/crear/', views.PelucheAnimalCreateView.as_view(), name='crear_peluche_animal'),
    path('animales/<int:pk>/', views.PelucheAnimalDetailView.as_view(), name='detalle_peluche_animal'),
    path('animales/<int:pk>/actualizar/', views.PelucheAnimalUpdateView.as_view(), name='actualizar_peluche_animal'),
    path('animales/<int:pk>/eliminar/', views.PelucheAnimalDeleteView.as_view(), name='eliminar_peluch_animal'),
]

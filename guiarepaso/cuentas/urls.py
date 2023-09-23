from django.urls import path
from cuentas.views import login, registro, CambiarContrasenia, PerfilView, editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/cambiar-contrasenia/', CambiarContrasenia.as_view(), name="cambiar_contrasenia"),
]

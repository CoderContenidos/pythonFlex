from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from cuentas.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from cuentas.models import InfoExtra


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            django_login(request, user)
            InfoExtra.objects.get_or_create(user=user)
            return render(request, "inicio/inicio.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()
    return render(request, "cuentas/login.html", {"form": form})

def registro(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            form = UserRegisterForm()     
      return render(request,"cuentas/registro.html" , {"form":form})
  

class PerfilView(TemplateView):
    template_name = "cuentas/perfil.html"


@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            usuario.infoextra.biografia = miFormulario.cleaned_data.get('biografia')
            if miFormulario.cleaned_data.get('avatar'):
                usuario.infoextra.avatar = miFormulario.cleaned_data.get('avatar')
            usuario.infoextra.save()
            miFormulario.save()
            return render(request, "cuentas/perfil.html")
    else:
        miFormulario = UserEditForm(initial={'avatar': usuario.infoextra.avatar, 'biografia': usuario.infoextra.biografia}, instance=request.user)
    return render(request, "cuentas/editar_perfil.html", {"form": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cuentas/cambiar_contrasenia.html'
    success_url = reverse_lazy('perfil')
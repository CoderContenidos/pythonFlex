from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from cuentas.forms import UserRegisterForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            django_login(request, user)            
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
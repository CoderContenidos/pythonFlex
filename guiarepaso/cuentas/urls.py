from django.urls import path
from cuentas.views import login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
]

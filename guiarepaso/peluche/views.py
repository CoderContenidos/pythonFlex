from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from peluche.models import PelucheAnimal
from peluche.forms import BusquedaPelucheAnimalFormulario


class PelucheAnimalCreateView(CreateView):
    model = PelucheAnimal
    fields = ['animal','altura','fecha', 'imagen', 'descripcion']
    template_name = "peluche/crear_peluche_animal.html"
    success_url = reverse_lazy('listado_peluches_animales')

class PelucheAnimalDeleteView(LoginRequiredMixin,DeleteView):
    model = PelucheAnimal
    template_name = "peluche/eliminar_peluche_animal.html"
    success_url = reverse_lazy('listado_peluches_animales')

class PelucheAnimalDetailView(DetailView):
    model = PelucheAnimal
    template_name = "peluche/detalle_peluche_animal.html"
    context_object_name = 'peluche'

class PelucheAnimalListView(ListView):
    model = PelucheAnimal
    template_name = "peluche/listado_peluches_animales.html"
    context_object_name = 'peluches_animales'
    
    def get_queryset(self):
        animal = self.request.GET.get('animal', '')
        if animal:
            peluches_animales = self.model.objects.filter(animal__icontains=animal)
        else:
            peluches_animales = self.model.objects.all()
        return peluches_animales

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaPelucheAnimalFormulario()
        context['palabra_de_busqueda'] = self.request.GET.get('animal', '')
        return context

class PelucheAnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = PelucheAnimal
    fields = ['animal','altura','fecha', 'imagen', 'descripcion']
    template_name = "peluche/actualizar_peluche_animal.html"
    success_url = reverse_lazy('listado_peluches_animales')

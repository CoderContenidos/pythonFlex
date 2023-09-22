from django import forms

class BusquedaPelucheAnimalFormulario(forms.Form):
    animal = forms.CharField(max_length=30, required=False)
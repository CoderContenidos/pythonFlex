from django import forms


class PaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=50)
    anio = forms.IntegerField()
    nueva = forms.BooleanField()
    
    
class PaletaFormularioBusqueda(forms.Form):
    modelo = forms.CharField(max_length=50, required=False)
from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateField()
    

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    nueva = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.marca} - {self.modelo}'
    
    
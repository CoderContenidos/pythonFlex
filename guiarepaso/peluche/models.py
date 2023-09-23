from django.db import models
from ckeditor.fields import RichTextField


class PelucheAnimal(models.Model):
    animal = models.CharField(max_length=30)
    altura = models.FloatField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='peluches', null=True, blank=True)
    descripcion = RichTextField(null=True)
    
    def __str__(self):
        return f'{self.animal}'
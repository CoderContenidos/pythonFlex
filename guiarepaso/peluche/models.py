from django.db import models


class PelucheAnimal(models.Model):
    animal = models.CharField(max_length=30)
    altura = models.FloatField()
    fecha = models.DateField()
    
    def __str__(self):
        return f'{self.animal}'
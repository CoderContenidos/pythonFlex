from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateField()
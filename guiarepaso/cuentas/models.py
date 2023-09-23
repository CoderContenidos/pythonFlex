from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank = True)
    biografia = models.TextField(null=True)
    
    def __str__(self):
        return f"Info extra del usuario {self.user}."


from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank = True)
    biografia = RichTextField(null=True)
    
    def __str__(self):
        return f"Info extra del usuario {self.user}."


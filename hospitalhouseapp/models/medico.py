from django.db import models
from .user import User

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Especialidad = models.CharField('Especialidad', max_length = 50, null= True)
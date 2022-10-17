from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Especialidad = models.CharField('Especialidad', max_length = 50, null= True)
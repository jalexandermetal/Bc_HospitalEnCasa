from django.db import models
from .user import User
from .medico import Medico
from .enfermero import Enfermero
from .historia import Historiaclinica



class Paciente(models.Model):
    id = models.BigAutoField(primary_key = True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    enfermo= models.ForeignKey(Enfermero, on_delete=models.CASCADE)
    historiaClinica =models.ForeignKey(Historiaclinica, on_delete=models.CASCADE)
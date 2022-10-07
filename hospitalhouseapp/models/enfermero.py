from email.policy import default
from django.db import models
from .user import User

class Enfermero(models.Model):
    id=models.BigAutoField(primary_key=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    area=models.CharField('Area', max_length=63)
    auxiliar=models.BooleanField('Auxiliar', default=False)
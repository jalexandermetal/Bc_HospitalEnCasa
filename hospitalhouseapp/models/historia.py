from django.db import models

class Historiaclinica(models.Model):
    id =models.BigAutoField(primary_key=True)
    oximetria = models.IntegerField('Oximetria', blank= True, null=True)
    frecuenciaRespiratoria = models.IntegerField('Frecuencia Respiratoria', blank= True, null=True)
    frecuenciaCardiaca = models.IntegerField('Frecuencia Cardiaca', blank= True, null=True)
    temperatura = models.IntegerField('Temperatura', blank= True, null=True)
    presionArterial = models.IntegerField('Presion Arterial', blank= True, null=True)
    glicemias = models.IntegerField('Glicemia', blank= True, null=True)
    diagnostico = models.TextField('diagnostico', blank=True)
    cuidados = models.TextField('cuidados', blank=True)
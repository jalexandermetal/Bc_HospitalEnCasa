from django.contrib import admin
from .models.usuario import Usuario
from .models.enfermero import Enfermero
from .models.historia import Historiaclinica
from .models.medico import Medico
from .models.paciente import Paciente

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Enfermero)
admin.site.register(Historiaclinica)
admin.site.register(Medico)
admin.site.register(Paciente)
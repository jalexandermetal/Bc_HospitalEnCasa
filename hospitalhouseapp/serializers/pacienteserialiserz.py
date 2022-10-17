from dataclasses import fields
from rest_framework import serializers
from hospitalhouseapp.models.paciente import Paciente

class Pacienteserializers(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields ='__all__'
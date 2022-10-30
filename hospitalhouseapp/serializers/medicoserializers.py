from dataclasses import fields
from rest_framework import serializers
from hospitalhouseapp.models.medico import Medico

class Medicoserializers(serializers.ModelSerializer):
    class Meta:
        models= Medico
        fields= '__all__'
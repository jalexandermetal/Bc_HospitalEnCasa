from dataclasses import field
from rest_framework import serializers
from hospitalhouseapp.models.enfermero import Enfermero

class Enfermeroserializers(serializers.ModelSerializer):
    class meta:
        model=Enfermero
        field='__all__'

from rest_framework import serializers
from hospitalhouseapp.models.usuario import Usuario

class Usuarioserializers(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'
from rest_framework import serializers
from hospitalhouseapp.models.historia import Historiaclinica

class Historiaclinicaserializers(serializers.ModelSerializer):
    class Meta:
        model=Historiaclinica
        fields='__all__'




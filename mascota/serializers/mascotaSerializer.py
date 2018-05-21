from rest_framework import serializers

from mascota.models import Mascota, Raza
from cliente.models import Cliente

# Create all serializers here
class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    raza = RazaSerializer()
    class Meta:
        model = Mascota
        fields = ('owner', 'mascotaId', 'nombreMascota', 'observaciones', 'fechaNacimiento', 'peso', 'altura','raza', 'especie')
        depth = 1

from rest_framework import serializers

from mascota.models import Mascota, Raza
from cliente.models import Cliente

# Create all serializers here
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('clienteId',)

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    raza = RazaSerializer()
    class Meta:
        model = Mascota
        fields = ('cliente','mascotaId', 'nombre', 'observaciones', 'fechaNacimiento','raza', 'especie')
        depth = 1

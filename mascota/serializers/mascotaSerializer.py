from rest_framework import serializers

from mascota.models import Mascota, Especie

# Create all serializers here
'''
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
'''

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ('nombre','tipoEspecie')


class PetSerializer(serializers.ModelSerializer):
    #mascota = MascotaSerializer()
    especie = EspecieSerializer()
    class Meta:
        model = Mascota
        fields = ('nombre', 'observaciones', 'fechaNacimiento', 'especie','raza')
        depth = 1

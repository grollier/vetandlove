#from django.core import serializers
from rest_framework import serializers

from cliente.models import Cliente, Correo, Direccion

# Create all your models here
'''
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
'''

class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ('correo',)

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    correo = CorreoSerializer()
    class Meta:
        model = Cliente
        fields = ('clienteId','nombre','apellido','dpi','password','fechaNacimiento', 'correo',)
        depth = 2

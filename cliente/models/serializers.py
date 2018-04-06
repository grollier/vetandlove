from rest_framework import serializers
from .cliente import Cliente
from .correo import Correo
from .telefono import Telefono

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = '__all__'

class CorreoSerializer(serializers.ModelSerializer):
     
     cliente = ClienteSerializer()
     class Meta:
         model = Correo
         fields = ('correoId', 'correo', 'cliente')


class TelefonoSerializer(serializers.ModelSerializer):
     cliente = ClienteSerializer()
     class Meta:
         model = Telefono
         fields = ('telefonoId', 'telefono', 'tipoTelefono', 'cliente')
         depth = 1

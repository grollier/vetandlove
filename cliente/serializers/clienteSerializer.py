#from django.core import serializers
from rest_framework import serializers

from cliente.models import Cliente, Correo, Direccion
from mascota.models import Mascota, Raza

# Create all your models here
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
        fields = ('clienteId','nombreCliente','apellido', 'password','fechaNacimiento', 'email', 'mascotas', 'direcciones', 'ordenes')
        depth = 2

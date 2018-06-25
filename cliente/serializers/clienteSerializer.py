#from django.core import serializers
from rest_framework import serializers

from cliente.models import Cliente, Direccion
from mascota.models import Mascota, Raza

# Create all your models here
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('clienteId','nombreCliente','apellido', 'password','fechaNacimiento', 'email', 'mascotas', 'direcciones', 'orden_cliente','estado_orden', 'servicio_orden')
        depth = 2

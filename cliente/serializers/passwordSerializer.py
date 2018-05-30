from rest_framework import serializers

from cliente.models import Cliente

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('clienteId', 'password')

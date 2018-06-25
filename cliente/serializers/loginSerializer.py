from rest_framework import serializers

from cliente.models import Cliente

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('email', 'password')

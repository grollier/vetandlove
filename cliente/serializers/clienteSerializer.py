#from django.core import serializers
from rest_framework import serializers

from cliente.models import Cliente

# Create all your models here
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

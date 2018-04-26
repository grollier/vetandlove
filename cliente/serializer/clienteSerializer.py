# Place your Serializer model here
from .models import Cliente

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        depth = 1

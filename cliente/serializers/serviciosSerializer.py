from rest_framework import serializers

from mascota.models import Mascota
from ordenDeTrabajo.models import Servicio

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('mascotaId', 'owner', 'servicio_mascota')
        depth = 1

from django.db import models

from .especie import Especie
from .kennel import Kennel

class Raza(models.Model):
    razaId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    origen = models.CharField(max_length=130)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, default=False)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE, default=False)

    def __str__(self):
       return "%s " % self.nombre
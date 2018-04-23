#Create your models here
from django.db import models

from .tipoServicio import Tipos
from .ordenT import Orden

class Servicio(models.Model):
    servicioId = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=230)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    tipoServicio = models.ForeignKey(Tipos, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.servicio

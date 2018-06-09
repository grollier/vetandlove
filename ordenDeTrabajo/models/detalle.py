#Create your models here
from django.db import models

from .servicio import Servicio
from .ordenT import Orden
class Detalle(models.Model):
    detalleId = models.AutoField(primary_key=True)
    detalle = models.OneToOneField(Orden, on_delete=models.CASCADE, default=False)
    tipoServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    

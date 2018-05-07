from django.db import models

from .ordenT import Orden

class Tipos(models.Model):
    tipoId = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=140,)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return "%s " % self.tipo 

from django.db import models

from .especie import Especie

class Kennel(models.Model):
    kennelId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    kennel = models.ManyToManyField(Especie, through='Raza')

    def __str__(self):
        return "%s " % self.nombre
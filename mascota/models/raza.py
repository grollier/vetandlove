# Create your models here
import datetime

from django.db import models
from django.utils import timezone

class Especie(models.Model):
    especieId = models.AutoField(primary_key=True)
    PERRO = 'perro'
    GATO = 'gato'
    OTROS = 'otro'
    TIPO_ESPECIE = (
       (PERRO, 'Perro'),
       (GATO, 'Gato'),
       (OTROS, 'Otros'),
    )
    tipoEspecie = models.CharField(max_length=5, choices=TIPO_ESPECIE)

    def __str__(self):
        return "%s " % self.tipoEspecie

class Kennel(models.Model):
    kennelId = models.AutoField(primary_key=True)
    nombre_kennel = models.CharField(max_length=128)
    kennel = models.ManyToManyField(Especie, through='Raza')

    def __str__(self):
        return "%s " % self.nombre

class Raza(models.Model):
    razaId = models.AutoField(primary_key=True)
    nombre_raza = models.CharField(max_length=128)
    origen = models.CharField(max_length=130)
    especie_raza = models.ForeignKey(Especie, on_delete=models.CASCADE, default=False, related_name='especies')
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE, default=False, related_name='kennels')

    def __str__(self):
       return "%s " % self.nombre_raza

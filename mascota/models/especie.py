# Create your models here
from django.db import models

class Especie(models.Model):
    especieId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    TIPO_ESPECIE = (
       ('P', 'PERRO'),
       ('G', 'GATO'),
       ('O', 'OTRO'),      
    )
    tipoEspecie = models.CharField(max_length=1, choices=TIPO_ESPECIE)
    
    def __str__(self):
        return "%s " % self.tipoEspecie

class Kennel(models.Model):
    kennelId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    kennel = models.ManyToManyField(Especie, through='Raza')

class Raza(models.Model):
    razaId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    origen = models.CharField(max_length=128)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, default=False)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE, default=False)


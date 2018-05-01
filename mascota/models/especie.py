# Create your models here
from django.db import models

class Especie(models.Model):
    especieId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    TIPO_ESPECIE = (
       ('Perro', 'PERRO'),
       ('Gato', 'GATO'),
       ('Otros', 'OTRO'),      
    )
    tipoEspecie = models.CharField(max_length=5, choices=TIPO_ESPECIE)
    
    def __str__(self):
        return "%s " % self.tipoEspecie

class Kennel(models.Model):
    kennelId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    kennel = models.ManyToManyField(Especie, through='Raza')

    def __str__(self):
        return "%s " % self.kennel

class Raza(models.Model):
    razaId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    origen = models.CharField(max_length=130)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, default=False)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE, default=False)

    def __str__(self):
       return "%s " % self.nombre

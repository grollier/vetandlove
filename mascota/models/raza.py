# create your models here
import datetime

from django.db import models

class Raza(models.Model)
    razaId = models.IntegerField(primary_key=True)
    raza = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)

class Group(models.Model):
    nombre = models.CharField(max_length=128)
    miembros = models.ManyToMany(Raza, trough='Kennel')


class Kennel(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    raza =  models.ForeignKey(Raza, on_delete=models.CASCADE, primary_key=True)
    razon = models.CharField(max_length=240)
    

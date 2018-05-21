# Create your models here
import datetime

from django.db import models
from django.utils import timezone

from .raza import Raza, Especie
from cliente.models import Cliente

class Mascota(models.Model):
    mascotaId = models.AutoField(primary_key=True)
    nombreMascota = models.CharField('Nombre', max_length=50)
    observaciones = models.TextField(max_length=240, blank=True, null=True)
    fechaNacimiento = models.DateField('Fecha de Nacimiento')
    peso = models.DecimalField('Peso',max_digits=5, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField('Altura',max_digits=5, decimal_places=2, blank=True, null=True)
    fechaCreacion = models.DateTimeField('publicado en',auto_now_add=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, default=False)
    owner = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')    

    def __str__(self):
        return "%s " % (self.nombreMascota)

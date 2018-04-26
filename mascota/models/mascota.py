# Create your models here
import datetime

from django.db import models
from django.utils import timezone

from .especie import Especie, Raza
from cliente.models import Cliente
class Mascota(models.Model):
    mascotaId = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=50)
    observaciones = models.CharField(max_length=240)
    fechaNacimiento = models.DateField('Fecha de Nacimiento')
    fechaCreacion = models.DateTimeField('publicado en',auto_now_add=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raza = models.OneToOneField(Raza, on_delete=models.CASCADE, default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return "%s " % (self.nombre)

    list_display = ('nombre', 'fechaNacimiento', 'cliente', 'especie', 'fechaCreacion')

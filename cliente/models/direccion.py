from django.db import models
from django import forms

from .zona import Zona
from .municipio import Municipio
from .cliente import Cliente

class Direccion(models.Model):
    direccionId = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=240)
    colonia = models.CharField(max_length=100)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, default=False)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')


def __str__(self):
    return '%s %s' % (self.direccion, self.colonia)

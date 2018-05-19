from __future__ import unicode_literals
from django import forms

from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombreCliente = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    password = models.CharField(max_length=12, default='132435',editable=True)
    fechaNacimiento = models.DateField()
    fechaCreacion = models.DateTimeField('publicado_en', auto_now=True)

    def __str__(self):
        return "%s " % self.nombre

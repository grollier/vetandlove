from __future__ import unicode_literals
from django import forms

from django.db import models
from django.utils import timezone


# Create your models here.
class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    dpi = models.CharField('DPI', max_length=13, unique=True)
    fechaNacimiento = models.DateField()
    fechaCreacion = models.DateTimeField('publicado_en', auto_now=True)


class FormCliente(forms.ModelForm):
    class Meta:
          model = Cliente
          fields = '__all__'

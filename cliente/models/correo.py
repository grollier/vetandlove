from django.db import models
from django.core.validators import EmailValidator
from django import forms

from .cliente import Cliente

class Correo(models.Model):
    correoId = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100, validators=[EmailValidator(message="Correo Invalido")])
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return "%s " % self.correo

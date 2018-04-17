from django.db import models
from django.core.validators import EmailValidator
from django import forms

from .cliente import Cliente

class Correo(models.Model):
    correoId = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100, validators=[EmailValidator(message="Correo Invalido")])
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)

class FormaCorreo(forms.ModelForm):
    class Meta:
          model = Correo
          fields = '__all__'

from django.db import models
from django import forms

from .cliente import Cliente

class Telefono(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefonoId = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=8, unique=True)
    TIPO_TELEFONO = (
         ('celular','CELULAR'),
         ('trabajo','TRABAJO'),
         ('casa','CASA'),
         ('otro','OTRO'),
    )
    tipodeTelefono = models.CharField(
     max_length = 7,
     default='CELULAR',
     choices = TIPO_TELEFONO
    )

class FormTelefono(forms.ModelForm):
    class Meta:
          model = Telefono
          fields = ('telefono', 'tipodeTelefono')
          exclude = ('telefonoId',) 

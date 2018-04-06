from django.db import models
from .cliente import Cliente

class Telefono(models.Model):
    telefonoId = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=8)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    TIPO_TELEFONO = (
         ('celular','CELULAR'),
         ('trabajo','TRABAJO'),
         ('casa','CASA'),
         ('otro','OTRO'),
    )
    tipodTelefono = models.CharField(
     max_length = 7,
     default='CELULAR',
     choices = TIPO_TELEFONO
    )

    def __str__(self):
        return "Usuario: %s %s %s" % (self.cliente.nombre, self.telefono.tipoTelefono)

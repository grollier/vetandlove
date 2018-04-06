from django.db import models
from django.utils import timezone
from .cliente import Cliente

# Create your models here.
class Correo(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    correoId = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return "Usuario: %s %s" % (self.cliente.nombre, self.correo)

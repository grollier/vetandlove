from django.db import models
from django import forms

from cliente.models import Cliente
from mascota.models import Mascota
from .estado import Estado
#Create your models here.
class Orden(models.Model):
    ordenId = models.AutoField(primary_key=True)
    horaRecepcion = models.TimeField('Hora Recepcion',auto_now=False)
    horaEntregaAproximada = models.TimeField('Entrega Aproximada',auto_now=False)
    horaEntrega = models.TimeField('Entrega',auto_now=False, blank=True,)
    facturaAsociada = models.CharField('Fact Asociada', max_length=240)
    observaciones = models.TextField('Observaciones',max_length=500)
    fechaCreacion = models.DateTimeField('Creada en', auto_now=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


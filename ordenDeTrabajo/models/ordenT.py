from django.db import models
from django import forms

from cliente.models import Cliente
from mascota.models import Mascota
from .estado import Estado

#Create your models here.
class Orden(models.Model):
    ordenId = models.AutoField(primary_key=True)
    nombreOrden = models.CharField(max_length=16, default='Orden de Compra')
    horaRecepcion = models.TimeField('Hora_Recepcion',auto_now=False)
    horaEntregaAproximada = models.TimeField('Entrega_Aproximada',auto_now=False)
    horaEntrega = models.TimeField('Entrega',auto_now=False)
    facturaAsociada = models.CharField(max_length=240)
    observaciones = models.TextField('Observaciones',max_length=500, blank=True)
    fechaCreacion = models.DateTimeField('Creada_en', auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.nombreOrden, self.ordenId) 

from django.db import models
from django import forms
from django.utils import timezone

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
    facturaAsociada = models.CharField(max_length=240, blank=True, null=True)
    observaciones = models.TextField('Observaciones',max_length=500, blank=True, null=True)
    fechaCreacion = models.DateTimeField('Creada_en', auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='orden_cliente')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='orden_mascota')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def mascotas_por_cliente(self):
        return self.mascota.objects.filter(owner)
    
    def hora_aproximada(self):
        return self.horaEntregaAproximada >= timezone.now() + datetime.timedelta(hours=2)

    def _str__(self):
        return "%s " % (self.nombreOrden, self.ordenId)

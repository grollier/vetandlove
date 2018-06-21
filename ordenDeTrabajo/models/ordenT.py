from django.db import models
from django import forms
from django.utils import timezone

from .servicio import Servicio
from cliente.models import Cliente

#Create your models here. 
class Estado(models.Model):
    NUEVA = 'N'
    ACTIVA = 'A'
    FINALIZADA = 'F'
    CANCELADA = 'C'
    ESTADOS_ORDENES = (
         (NUEVA, 'Nueva'),
         (ACTIVA, 'Activa'),
         (FINALIZADA, 'Finalizada'),
         (CANCELADA, 'Cancelada'),
    )
    estados = models.CharField(max_length=2, choices=ESTADOS_ORDENES, help_text='Estado de la Orden',)
    
    def __str__(self):
       return self.estado

class Orden(models.Model):
    ordenId = models.AutoField(primary_key=True)
    nombreOrden = models.CharField(max_length=16, default='Orden de Compra')
    horaRecepcion = models.TimeField('Hora_Recepcion',auto_now=False)
    horaEntregaAproximada = models.TimeField('Entrega_Aproximada',auto_now=False)
    horaEntrega = models.TimeField('Entrega',auto_now=False)
    facturaAsociada = models.CharField(max_length=240, blank=True, null=True)
    observaciones = models.TextField('Observaciones',max_length=500, blank=True, null=True)
    fechaCreacion = models.DateTimeField('Creada_en', auto_now_add=True)
    estado_orden = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='estado')
    servicio_orden = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='servicio_de_orden', default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordenes', default=False)
    
    def hora_aproximada(self):
        hora_entrega = self.horaEntregaAproximada
        return hora_entrega + datetime.timedelta(hours=2)

    def _str__(self):
        return "%s " % (self.nombreOrden, self.ordenId)

from  django.db import models
from django import forms
from django.utils import timezone

from .ordenT import Orden

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
    ordenes = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='estado_ordenes',default=False)

    def __str__(self):
       return self.estados


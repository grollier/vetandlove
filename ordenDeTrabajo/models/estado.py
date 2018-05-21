from django.db import models
from django import forms

class Estado(models.Model):
    ESTADOS_ORDENES = (
         ('Nueva', 'NUEVA'),
         ('Activa', 'ACTIVA'),
         ('Finalizada','FINALIZADA'),
         ('Cancelada','CANCELADA'),
    )
    estado = models.CharField(max_length=10, choices=ESTADOS_ORDENES, help_text='Estado de la orden actual',)
    
    def __str__(self):
        return self.estado


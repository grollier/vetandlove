# Create your models here
import datetime

from django.db import models
from django.utils import timezone
from cliente.models.cliente import Cliente
from .raza import Raza

class Mascota(models.Model):
    mascotaId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=240)
    fechaNacimiento = models.DateField()
    fechaCreacion = models.DateTimeField('publicado en')
    cliente = models.ForeignKey(Cliente, on_delete=CASACADE,)
    raza = models.OneToOneField(Raza, on_delete=CASCADE,)
    
    def was_punlished_recently(self):
        return self.fechaCreacion >= tiemzone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return "%s %s %S" % (self.nombre, self.raza, self.cliente,)

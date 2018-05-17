from django.db import models

class Especie(models.Model):
    especieId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    tipoEspecie = models.CharField(max_length=5)
    
    def __str__(self):
        return "%s " % self.tipoEspecie
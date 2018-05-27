from django.db import models

# Create your models here
class Promociones(models.Model):
    titulo = models.CharField(max_length=128)
    textoPromocion = models.CharField(max_length=300)
    

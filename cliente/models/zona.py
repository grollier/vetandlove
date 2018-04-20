from django.db import models

class Zona(models.Model):
    zonaId = models.AutoField(primary_key=True)
    zona = models.CharField(max_length=2)

    def __str__(self):
        return self.zona

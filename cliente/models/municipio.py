from django.db import models

class Municipio(models.Model):
    municipioId = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=50)

    def __str__(self):
        return self.municipio

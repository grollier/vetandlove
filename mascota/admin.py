from django.contrib import admin

from django.db import models
from models.mascota import Mascota
from models.raza import Raza, Grupo, Kennel
# Register your models here.
myModels = [Mascota, Raza, Grupo, Kennel]
admin.site.register(myModels)

from django.contrib import admin

from django.db import models
from .models import *

# Register your models here.
myModels = [Mascota]

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza', 'fechaNacimiento', 'cliente', 'especie', 'fechaCreacion')
admin.site.register(myModels, MascotaAdmin,)

from django.contrib import admin

from django.db import models
from .models import *

# Register your models here.
myModels = [Mascota]

class MascotaAdmin(admin.ModelAdmin):
    model = Mascota
    fieldsets = (
        ('Nombre del Dueño', {
            'fields': ('owner',)
        }),
        ('Informacion de la Mascota', {
            'fields': ('nombreMascota', 'fechaNacimiento', ('especie', 'raza'), ('peso', 'altura'))
        }),
        ('observaciones', {
             'classes': ('collapse',),
             'fields': ('observaciones',),
        }),
    )
    list_display = ('nombreMascota', 'raza', 'especie', 'owner')
    search_fields = ('nombreMascota', 'raza', 'owner')

admin.site.register(myModels, MascotaAdmin)

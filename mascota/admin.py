from django.contrib import admin

from django.db import models
from .models import *

# Register your models here.
myModels = [Mascota]

class MascotaAdmin(admin.ModelAdmin):
    model = Mascota
    fieldsets = (
        ('Nombre del Dueño', {
            'fields': ('cliente',)
        }),
        ('Informacion de la Mascota', {
            'fields': ('nombreMascota', 'fechaNacimiento', 'especie', 'raza',)
        }),
        ('Observacions', {
            'classes': ('collapse',),
            'fields': ('observaciones',),
        }),
    )
    list_display = ('nombreMascota', 'raza', 'especie', 'cliente')
    search_fields = ('nombreMascota', 'raza', 'cliente')

admin.site.register(myModels, MascotaAdmin)

from django.contrib import admin

from django.db import models
from .models import *

# Register your models here.
myModels = [Mascota]

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre','raza', 'fechaNacimiento', 'cliente', 'especie', 'fechaCreacion')
admin.site.register(myModels, MascotaAdmin,)

class EspecieAdmin(admin.ModelAdmin):
    ##inlines = [CorreoInline, TelefonoInline, DireccionInline]
    list_display = ('nombre', 'tipoEspecie')
    search_fields = ('nombre','tipoEspecie')
admin.site.register(Especie, EspecieAdmin,)

class RazaAdmin(admin.ModelAdmin):
    ##inlines = [CorreoInline, TelefonoInline, DireccionInline]
    list_display = ('nombre', 'origen', 'especie', 'kennel')
    search_fields = ('nombre','origen', 'especie', 'kennel')
admin.site.register(Raza, RazaAdmin,)

class KennelAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(Kennel, KennelAdmin,)
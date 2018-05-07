from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from django.db import models
from .models import Orden, Servicio, Tipos, Estado, Detalle
from cliente.models import Cliente
from mascota.models import Mascota

# Register your models here.
class ServicioInline(admin.TabularInline):
    model = Servicio
    exclude = ('tipoServicio',)
    max_num = 1

class TiposInline(admin.TabularInline):
    model = Tipos
    max_num = 1
"""
class DetalleInline(admin.TabularInline):
    model = Detalle
"""

class OrdenInline(admin.ModelAdmin):
    inlines = [ServicioInline,TiposInline,]
    list_display= ('cliente', 'mascota', 'horaRecepcion', 'horaEntrega', 'estado', 'fechaCreacion')
admin.site.register(Orden, OrdenInline)
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from django.db import models
from .models import Orden, Servicio, Estado, Detalle
from cliente.models import Cliente
from mascota.models import Mascota

# Register your models here.
class ServicioInline(admin.TabularInline):
    model = Servicio
    max_num = 1
    exclude = ('tipoServicio',)
'''
class DetalleInline(admin.TabularInline):
    model = Detalle
'''

class OrdenInline(admin.ModelAdmin):
    inlines = [ServicioInline,]
    exclude = ('nombreOrden',)
    list_display = ('cliente', 'mascota', 'estado', 'fechaCreacion', 'facturaAsociada')
admin.site.register(Orden, OrdenInline)

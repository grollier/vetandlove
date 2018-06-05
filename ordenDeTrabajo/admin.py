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
'''
class ClienteOrden(admin.TabularInline):
    model = Orden
    fields = ('orden_cliente',)
'''

def mascota(Mascota):
  mascota = Mascota.objects.filter(mascota=owner)
  return ("%s ") % mascota.self

class OrdenInline(admin.ModelAdmin):
    inlines = [ServicioInline]
    exclude = ('nombreOrden',)
    list_display = ('cliente', 'mascota', 'estado', 'fechaCreacion', 'facturaAsociada')
    fieldsets = (
        ('Datos de Orden', {
            'fields': ['horaRecepcion', 'horaEntregaAproximada', 'horaEntrega', 'estado']
        }),
        ('Cliente', {
            'fields': ['cliente','mascota']
        }),
        ('Datos Adicionales', {
            'classes': ('extrapretty',),
            'fields': ('facturaAsociada', 'observaciones'),
        }),
    )
admin.site.register(Orden, OrdenInline)

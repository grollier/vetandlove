from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from django.db import models
from .models import *

# Register your models here.
class EstadoInline(admin.TabularInline):
    model = Estado
    fields = ('estados',)
    max_num = 1

class ServiciosInline(admin.TabularInline):
    model = Servicio
    fields = ('servicios','mascota_servicio', 'precio_servicio')
    max_num = 1

class OrdenAdmin(admin.ModelAdmin):
    fieldsets  = (
        ('Orden Nueva', {'fields': ('cliente',)}),
        ('Ingrese Horario', {'fields': ('horaRecepcion', 'horaEntregaAproximada', 'horaEntrega')}),
        ('factura Asociada', {'fields': ('facturaAsociada',)}),
        ('observasiones', {'classes': ('collapse',),
                'fields': ('observaciones',)}),
    )
    inlines = [ServiciosInline, EstadoInline]
admin.site.register(Orden, OrdenAdmin)

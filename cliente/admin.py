from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.db import models

from .models import Cliente, Correo, Telefono, Direccion, Municipio, Zona
from mascota.models import Mascota

# Register your models here.

class DireccionInline(admin.TabularInline):
    model = Direccion
    max_num = 1

class CorreoInline(admin.TabularInline):
    model = Correo

class TelefonoInline(admin.TabularInline):
    model = Telefono
    max_num = 1
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombreCliente', 'apellido' , 'email', 'is_active')
    list_filter = ('nombreCliente', 'is_active')
    fieldsets = (
        ('Cliente Nuevo', {'fields': ('nombreCliente', 'apellido', 'email')}),
        (None, {'fields': ('fechaNacimiento',)}),
        ('Estatus', {
            'classes': ('extrapetty',),
            'fields': ('is_active',),
        }),
    )
    search_fields = ('nombreCliente', 'email', 'mascotas')
admin.site.register(Cliente, ClienteAdmin,)

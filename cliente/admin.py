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
    inlines = [CorreoInline, TelefonoInline, DireccionInline]
    list_display = ('nombre', 'dpi', 'fechaCreacion')
    search_fields = ('nombre','dpi','fechaCreacion')
    exclude = ('password',)
admin.site.register(Cliente, ClienteAdmin,)

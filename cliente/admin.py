from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.db import models

from .models import Cliente, Correo, Telefono

# Register your models here.
class CorreoInline(admin.TabularInline):
    model = Correo

class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 0
    
class ClienteAdmin(admin.ModelAdmin):
    inlines = [CorreoInline, TelefonoInline]
    list_display = ('clienteId', 'nombre', 'dpi', 'fechaCreacion')

admin.site.register(Cliente, ClienteAdmin)

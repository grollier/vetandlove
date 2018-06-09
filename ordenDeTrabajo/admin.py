from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from django.db import models
from .models import Orden, Servicio, Estado, Detalle

# Register your models here.
class OrdenInline(admin.TabularInline):
    model = Orden
    max_num = 1
    exclude = ('ordenId', 'nombreOrden')

class ServicioAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': 'servicio'})]

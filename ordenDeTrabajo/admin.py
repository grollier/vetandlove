from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from django.db import models
from .models import Servicio

# Register your models here.

admin.site.register(Servicio)

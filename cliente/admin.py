from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.db import models

from .models import Cliente, Telefono, Direccion, Municipio, Zona
from mascota.models import Mascota

# Register your models here.
class DireccionInline(admin.TabularInline):
    model = Direccion
    max_num = 1


#class CorreoInline(admin.TabularInline):
#   model = Correo

class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 0

#@admin.register(Cliente)
class ClienteCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ('username', 'email')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 - self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("La contrasena no es la misma")
        return password2

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return

class ClienteChangeForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombreCliente', 'email','password', 'fechaCreacion', 'is_active',)
   
    def clean_password(self):
        return self.initial["password"]


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteChangeForm
    add_form = ClienteCreationForm

    list_display = ('username','nombreCliente','email','fechaCreacion',)
    list_filter = ('username', 'nombreCliente')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informacion Personal', {'fields': ('nombreCliente','apellido','fechaNacimiento', 'fechaCreacion')}),
        ('Permisos', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
             'classes':('wide',),
             'fields': ('username', 'email', 'fechaCreacion', 'password1', 'password2')}
        ),
    )
    search_fields = ("username","nombreCliente","apellido")
    inlines = [TelefonoInline, DireccionInline]

admin.site.register(Cliente, ClienteAdmin)

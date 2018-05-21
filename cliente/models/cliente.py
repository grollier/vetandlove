from __future__ import unicode_literals

from django import forms
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(_('Nombre'), max_length=50)
    apellido = models.CharField(_('Apellido'), max_length=50)
    email = models.EmailField(_('Correo Electronico'),blank=True,null=True)
    is_active = models.BooleanField(
        _('Miembro Activo'),
        default=True,
        help_text=_("Designa si el Usuario es o no un miembro activo"
        ),
    )
    password = models.CharField(max_length=12, default=132435,editable=True)
    fechaNacimiento = models.DateField(_('Fecha de Nacimiento'),)
    fechaCreacion = models.DateTimeField(_('publicado en'), auto_now_add=True)
    las_edit = models.DateTimeField(_('updated_user'), default=timezone.now)

    def __str__(self):
        return "%s " % self.nombreCliente

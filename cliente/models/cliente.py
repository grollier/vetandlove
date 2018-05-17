from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

class ClienteManager(BaseUserManager):
    def create_cliente(self, username, email, fechaNacimiento, password):
        if not username:
            raise ValueError('Los clientes deben tener un nombre de usuario')
        

        cliente = self.model(
            username = self.normalize_username(username),
            email = delf.normalize_email(email),
            fechaNacimiento = fechaNacimiento,
        )

        cliente.set_password(password)
        cliente.save(using=self._db)
        return cliente

class Cliente(AbstractBaseUser):

    username_validator = UnicodeUsernameValidator()

    userId = models.AutoField(primary_key=True)
    username = models.CharField(
         _('DPI'),
         max_length=13,
         unique=True,
         help_text=_('Requiere el ingreso del DPI para uso de usuario'),
         validators=[username_validator],
         error_messages={
             'unique': _("El DPI ingresado ya existe, intente de nuevo"),
         },
    )
    nombreCliente = models.CharField(_('Nombre'), max_length=150,)
    apellido = models.CharField(_('Apellido'), max_length=150,)
    email = models.EmailField(_('Correo Electronico'),blank=True)
    is_active = models.BooleanField(
        _('Miembro Activo'),
        default=True,
        help_text=_(
         "Designa si el usuario es o no un miembro activo del sistema"
        ),
    )
    fechaNacimiento = models.DateField(_('Fecha de Nacimiento'),)
    fechaCreacion = models.DateTimeField(_('Publicado_en'), default=timezone.now)

    objects = ClienteManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','nombre','fecha de cliticos']

     
    def __str__(self):
        return self.nombreCliente

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
         return True

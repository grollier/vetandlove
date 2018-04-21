from django.contrib import admin

from django.db import models
from .models import *

# Register your models here.
myModels = [Mascota]
admin.site.register(myModels)

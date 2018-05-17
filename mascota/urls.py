from django.urls import path, include
from rest_framework import routers

from . import views

routerMascota = routers.DefaultRouter()
routerMascota.register(r'mascota', views.MascotaViewSet)
routerMascota.register(r'especie', views.EspecieViewSet)
routerMascota.register(r'raza', views.RazaViewSet)
routerMascota.register(r'kennel', views.KennelViewSet)
from django.urls import path
from rest_framework import routers

from . import views
from . import views

routerCliente = routers.DefaultRouter()
routerCliente.register(r'cliente', views.ClienteViewSet)
routerCliente.register(r'direccion', views.DireccionViewSet)
routerCliente.register(r'pass-check', views.PassCheckViewSet)

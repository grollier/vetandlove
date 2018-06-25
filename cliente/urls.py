from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from . import views

routerCliente = routers.DefaultRouter()
urlpatterns = [
]
routerCliente.register(r'cliente', views.ClienteViewSet)
routerCliente.register(r'direccion', views.DireccionViewSet)
routerCliente.register(r'servicios', views.ServiciosViewSet)
routerCliente.register(r'cambio_pass', views.PassCheckViewSet)
routerCliente.register(r'login', views.LoginViewSet)


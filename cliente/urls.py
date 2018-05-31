from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from . import views

routerCliente = routers.DefaultRouter()
urlpatterns = [
    url(r'^signup/', views.pass_confirm, name='pass_check')
]
routerCliente.register(r'cliente', views.ClienteViewSet)
routerCliente.register(r'direccion', views.DireccionViewSet)
routerCliente.register(r'cliente-p/$', views.PassCheckViewSet)


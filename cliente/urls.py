# Create all your URLs here
from django.urls import path

from . import views

urlpatterns = [
    path('clientes', views.cliente_json, name='clientes'),
]

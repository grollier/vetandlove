from django.urls import path

from . import views

urlpatterns = [
   path('', views.clienteList.as_view(), name='clientes'),
]

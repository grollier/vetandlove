from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cliente, Direccion
from mascota.models import Mascota

from .serializers import UserSerializer, DireccionSerializer, PassSerializer, LoginSerializer, ServiciosSerializer

# Create your views here.
class LoginViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = LoginSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = UserSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class PassCheckViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = PassSerializer

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = ServiciosSerializer

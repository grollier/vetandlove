from django.shortcuts import render

from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cliente, Direccion
from .serializers import UserSerializer, DireccionSerializer, PassSerializer

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = UserSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class PassCheckViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = PassSerializer

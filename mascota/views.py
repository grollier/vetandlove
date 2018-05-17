from django.shortcuts import render

from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mascota, Especie, Raza, Kennel
from .serializers import PetSerializer

# Create your views here.
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = PetSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    #serializer_class = PetSerializer

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()

class KennelViewSet(viewsets.ModelViewSet):
    queryset = Kennel.objects.all()
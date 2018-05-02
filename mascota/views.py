from django.shortcuts import render

from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mascota
from .serializers import PetSerializer

# Create your views here.
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = PetSerializer

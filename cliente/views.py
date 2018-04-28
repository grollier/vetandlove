from django.shortcuts import render

from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cliente
from .serializers import ClienteSerializer

# Create your views here.
class clienteList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

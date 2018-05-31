from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cliente, Direccion
from .forms import FormPassConfirmation

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

def pass_confirm(request, template='clientes/pass_confirmation.html'):
    if request.method == 'POST':
        form = FormPassConfirmation(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            user = Cliente(username=nombreCliente)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('usuarios/cliente')
    else:
        form = FormPassConfirmation()

    return render(request, template, {'form':form}) 

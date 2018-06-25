from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from ordenDeTrabajo.models import Orden, Estado, Servicio

# views for the orders
class IndexView(generic.ListView):
    context_object_name = 'ordenes'
    template_name = 'ordenDeTrabajo/templates'
    
    def get_queryset(self):
        return Orden.objects.all()

class OrdenEntry(CreateView):
    model = Orden
    fields = ['horaRecepcion', 'horaEntregaAproximada', 'horaEntrega', 'facturaAsociada', 'observaciones']

class EstadoEntry(CreateView):
    model = Estado
    fields = ['estados',]

class ServicioEntry(CreateView):
    model = Servicio
    fields = ['servicios', 'precio_servicio', 'mascota_servicio',]

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Cliente, Componente, Producto, Pedido
from .forms import ClienteForm



#Ventana principal CAMBIAR A CLASE??

"""Pantalla principal"""
def principal(request):
    return render(request, 'principal.html')


#CLIENTE 

# Vista de listado de clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_listado.html'
    context_object_name = 'clientes'

# Vista de detalle de cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detalle.html'
    context_object_name = 'cliente'

# Vista de creación de cliente
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_listado')  # Esto es para que cuando lo cree vaya directamente al link de atras 

# Vista de eliminación de cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_eliminar.html'
    success_url = reverse_lazy('cliente_listado')



#COMPONENTES - De momento solo hay listado y detalle ya que no era un requisito, hacer mas tarde creacion y eliminacion??

# Vista de listado de componentes
class ComponenteListView(ListView):
    model = Componente
    template_name = 'componente_listado.html'
    context_object_name = 'componentes'

# Vista de detalle de cliente
class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente_detalle.html'
    context_object_name = 'componente'
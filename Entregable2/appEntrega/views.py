from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView
from .models import Cliente, Componente, Producto, Pedido
from .forms import ClienteForm,ProductoForm,PedidoForm,ComponenteForm

from django.contrib import messages
from django.core.mail import send_mail
from Entregable2.settings import DEFAULT_FROM_EMAIL




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
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_editar.html'
    success_url = reverse_lazy('cliente_listado')


#PRODUCTOS

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_listado.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name= 'producto_detalle.html'
    context_object_name = 'producto'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_listado')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.precio = self.object.calcular_precio()
        self.object.save()
        return response

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_eliminar.html'
    success_url = reverse_lazy('producto_listado')
    
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_editar.html'
    success_url = reverse_lazy('producto_listado')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.precio = self.object.calcular_precio()
        self.object.save()
        return response


# Función para calcular el precio de los componentes seleccionados
def calcular_precio_componentes(request):
    ids = request.GET.getlist('ids[]')
    componentes = Componente.objects.filter(id__in=ids)
    total = sum(c.precio for c in componentes)
    return JsonResponse({'total': float(total)})

#PEDIDOS

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_listado.html'
    context_object_name = 'pedidos'
    
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detalle.html'
    context_object_name = 'pedido'
    
class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_form.html'
    success_url = reverse_lazy('pedido_listado')

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedido_eliminar.html'
    success_url = reverse_lazy('pedido_listado')

class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_editar.html'
    success_url = reverse_lazy('pedido_listado')
    
    # Ejecuta si se edita con éxito, si se ha cambiado el estado del pedido saltará una notificación y enviará un email al cliente
    def form_valid(self, form):
        pedido = form.save(commit=False)
        pedido_anterior = Pedido.objects.get(pk=pedido.pk)
        estado_anterior = pedido_anterior.estado
        if form.cleaned_data['estado'] != estado_anterior:
            # Salta popup de aviso
            messages.success(
                self.request,
                f"El estado del pedido ha cambiado de {pedido_anterior.get_estado_display()} a {pedido.get_estado_display()}. Se enviará un email a la empresa."
            )
            # Enviar email
            cliente = pedido.cliente
            if cliente.datos_contacto:
                send_mail(
                    subject=f'El estado de su pedido {pedido.codigo_referencia} ha cambiado',
                    message=f'El estado del pedido {pedido.codigo_referencia} ha cambiado de {pedido_anterior.get_estado_display()} a {pedido.get_estado_display()}.',
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[cliente.datos_contacto],
                    fail_silently=False,
                )
        return super().form_valid(form)

#COMPONENTES 

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

class ComponenteCreateView(CreateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'componente_form.html'
    success_url = reverse_lazy('componente_listado')
    
class ComponenteDeleteView(DeleteView):
    model = Componente
    template_name = 'componente_eliminar.html'
    success_url = reverse_lazy('componente_listado')
    
class ComponenteUpdateView(UpdateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'componente_editar.html'
    success_url = reverse_lazy('componente_listado')


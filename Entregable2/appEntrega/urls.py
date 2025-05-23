from django.urls import path
from . import views
"""No olvidarse de importar todas las vistas creadas!!!!"""
from .views import principal
#Cliente
from .views import *

urlpatterns = [
#Principal
path('', principal, name='home'),

#Cliente
path('clientes/', ClienteListView.as_view(), name='cliente_listado'),
path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detalle'),
path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_crear'),
path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_eliminar'),
path("cliente/<int:pk>/editar/", ClienteUpdateView.as_view(), name="cliente_editar"),

#Producto
path("productos/", ProductoListView.as_view(), name="producto_listado"),
path("productos/<int:pk>/", ProductoDetailView.as_view(), name="producto_detalle"),
path("productos/nuevo/", ProductoCreateView.as_view(), name="producto_crear"),
path("productos/<int:pk>/eliminar/", ProductoDeleteView.as_view(), name="producto_eliminar"),
path("productos/<int:pk>/editar/", ProductoUpdateView.as_view(), name="producto_editar"),

#Pedido
path("pedidos/", PedidoListView.as_view(), name="pedido_listado"),
path("pedidos/<int:pk>/", PedidoDetailView.as_view(), name="pedido_detalle"),
path("pedidos/nuevo/", PedidoCreateView.as_view(), name="pedido_crear"),
path("pedidos/<int:pk>/eliminar/", PedidoDeleteView.as_view(), name="pedido_eliminar"),
path("pedidos/<int:pk>/editar/", PedidoUpdateView.as_view(), name="pedido_editar"),

#Componente
path('componente/',ComponenteListView.as_view(), name='componente_listado'),
path('componente/<int:pk>/', ComponenteDetailView.as_view(),name='componente_detalle'),
path('componente/nuevo/', ComponenteCreateView.as_view(), name='componente_crear'),
path('componente/<int:pk>/eliminar/', ComponenteDeleteView.as_view(), name='componente_eliminar'),
path('componente/<int:pk>/editar/', ComponenteUpdateView.as_view(), name='componente_editar'),

path('api/calcular-precio/', views.calcular_precio_componentes, name='calcular_precio_componentes'),

]

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

#Producto
path("productos/", ProductoListView.as_view(), name="producto_listado"),
path("productos/<int:pk>/", ProductoDetailView.as_view(), name="producto_detalle"),
path("productos/nuevo/", ProductoCreateView.as_view(), name="producto_crear"),
path("productos/<int:pk>/eliminar/", ProductoDeleteView.as_view(), name="producto_eliminar"),


#Componente
path('componente/',ComponenteListView.as_view(), name='componente_listado'),
path('componente/<int:pk>/', ComponenteDetailView.as_view(),name='componente_detalle'),
 
]

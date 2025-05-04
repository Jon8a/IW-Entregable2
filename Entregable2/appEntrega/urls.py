from django.urls import path
from . import views
"""No olvidarse de importar todas las vistas creadas!!!!"""
from .views import principal
#Cliente
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteDeleteView,
)
#Componente
from .views import(
    ComponenteDetailView,
    ComponenteListView
)

urlpatterns = [
#Principal
path('', principal, name='home'),

#Cliente
path('clientes/', ClienteListView.as_view(), name='cliente_listado'),
path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detalle'),
path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_crear'),
path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_eliminar'),

#Componente
path('componente/',ComponenteListView.as_view(), name='componente_listado'),
path('componente/<int:pk>/', ComponenteDetailView.as_view(),name='componente_detalle'),
 
]

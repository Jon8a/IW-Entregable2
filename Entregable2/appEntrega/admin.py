from django.contrib import admin

from .models import Cliente, Componente, Producto, Pedido

# Registra los modelos en el administrador
admin.site.register(Cliente)
admin.site.register(Componente)
admin.site.register(Producto)
admin.site.register(Pedido)
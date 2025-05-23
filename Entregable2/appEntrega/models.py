from django.db import models

"""SI CREAIS NUEVOS MODELOS AÑADIRLOS A LA PAGINA DE ADMINISTRADOR PARA CREAR REGISTROS MAS FACIL"""

"""Es el extra, valorar si merece la pena hacerlo"""
class Cliente(models.Model):
    cif = models.CharField(max_length=15, unique=True)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    datos_contacto = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre_empresa} ({self.cif})"


class Componente(models.Model):
    codigo_referencia = models.CharField(max_length=50, unique=True)
    nombre_modelo = models.CharField(max_length=100)
    tipo_componente = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    especificaciones_tecnicas = models.TextField()
    archivo = models.FileField(upload_to='componentes/', null=True, blank=True)

    def __str__(self):
        return self.nombre_modelo


class Producto(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    componentes = models.ManyToManyField(Componente, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    def calcular_precio(self):
        return sum(componente.precio for componente in self.componentes.all())



class Pedido(models.Model):

    ESTADO_OPCIONES = [
        ('en_proceso', 'En proceso'),
        ('preparado', 'Preparado'),
        ('entregado', 'Entregado'),
    ]

    URGENCIA_OPCIONES = [
        ('urgente', 'Urgente'),
        ('prioritario', 'Prioritario'),
        ('normal', 'Normal'),
    ]

    codigo_referencia = models.CharField(max_length=50, unique=True)
    fecha_entrega_estimada = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, related_name='pedidos')
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='en_proceso')
    urgencia = models.CharField(max_length=20, choices=URGENCIA_OPCIONES, default='normal')
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido {self.codigo_referencia} ({self.estado})"

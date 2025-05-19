from django import forms
from .models import Cliente,Producto,Pedido,Componente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cif', 'nombre_empresa', 'direccion', 'datos_contacto']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['referencia','precio' ,'nombre','descripcion' ,'categoria' , 'componentes' ]
        
class PedidoForm(forms.ModelForm):
     class Meta:
        model = Pedido
        fields = ['codigo_referencia','fecha_entrega_estimada',
                  'fecha_entrega','cliente','productos','estado','urgencia','detalles' ]
        widgets = {
            'fecha_entrega_estimada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),

        }

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['codigo_referencia','nombre_modelo','tipo_componente','proveedor','especificaciones_tecnicas']
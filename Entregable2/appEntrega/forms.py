from django import forms
from .models import Cliente,Producto,Pedido,Componente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cif', 'nombre_empresa', 'direccion', 'datos_contacto']
        widgets = {
            'cif': forms.TextInput(attrs={'class': 'mayusculas'})
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['referencia','nombre','descripcion' ,'categoria' , 'componentes', 'precio' ]
        widgets = {
            'referencia': forms.TextInput(attrs={'class': 'mayusculas'}),
            'precio': forms.NumberInput(attrs={'readonly': 'readonly'})
        }
        
class PedidoForm(forms.ModelForm):
     class Meta:
        model = Pedido
        fields = ['codigo_referencia','fecha_entrega_estimada',
                  'fecha_entrega','cliente','productos','estado','urgencia','detalles' ]
        widgets = {
            'codigo_referencia': forms.TextInput(attrs={'class': 'mayusculas'}),
            'fecha_entrega_estimada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),

        }

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['codigo_referencia','nombre_modelo','tipo_componente','proveedor','precio','especificaciones_tecnicas','archivo']
        widgets = {
            'codigo_referencia': forms.TextInput(attrs={'class': 'mayusculas'})
        }


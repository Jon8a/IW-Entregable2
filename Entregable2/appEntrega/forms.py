from django import forms
from .models import Cliente,Producto,Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cif', 'nombre_empresa', 'direccion', 'datos_contacto']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['referencia','precio' ,'nombre','descripcion' ,'categoria' , 'componentes' ]
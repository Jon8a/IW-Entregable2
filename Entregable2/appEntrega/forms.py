from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cif', 'nombre_empresa', 'direccion', 'datos_contacto']
from django import forms
from libreria.models import clientes

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)

class libreriaForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = ["nombre", "direccion", "numero_dni"]
from django import forms
from .models import *




class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = ["foto", "nombre", "precio", "categoria", "estado", "descripcion", "numero_telefonico"]

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

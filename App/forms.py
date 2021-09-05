from django import forms
from django.db.models.base import Model
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = ["foto", "nombre", "precio", "categoria", "estado", "descripcion", "fecha_Expiracion"]
    

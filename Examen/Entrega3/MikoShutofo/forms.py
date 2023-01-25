from django import forms
from django.forms import ModelForm 
from django.forms import widgets 
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import TipoCliente, Datos, Tipo, Producto


class DatosForm(forms.ModelForm): 
    class Meta: 
        model = Datos
        fields = ['rut', 'nombre', 'apellidoPat', 'apellidoMat', 'contato', 'correo', 'categoria']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellidoPat': 'Apellido Paterno',
            'apellidoMat': 'Apellido Materno',
            'contato': 'Contacto',
            'correo': 'Correo',
            'categoria': 'Categoria',

        }
        widgets={
            'rut': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite su rut',
                    'id': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Digite su nombre',
                    'id': 'nombre'
                }
            ),
            'apellidoPat': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Digite su apellido paterno',
                    'id': 'apellidoPat'
                }
            ),
            'apellidoMat': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Digite su apellido materno',
                    'id': 'apellidoMat'
                }
            ),
            'contato': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Número de contacto',
                    'id': 'contato'
                }
            ),
            'correo': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Correo Electrónico',
                    'id': 'correo'
                }
            ),
            'categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
        }

class ProductoForm(forms.ModelForm):    
    class Meta: 
        model= Producto
        fields = ['idproducto', 'nombre', 'tamaño', 'categoria', 'imagen']
        labels ={
            'idproducto': 'ID Producto', 
            'nombre': 'Nombre', 
            'tamaño': 'Tamaño en cm', 
            'categoria': 'Categoría',
            'imagen': 'Imagen'
        }
        widgets={
            'idproducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ID Producto', 
                    'id': 'idproducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'tamaño': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese tamaño en cm', 
                    'id': 'tamaño'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )    
        }

 

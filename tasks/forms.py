from django import forms
from .models import Tareas, Cliente, Stock


class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['trabajosolicitado', 'trabajoarealizar', 'observaciones', 'nombre', 'telefono']
        widgets = {
            'trabajosolicitado': forms.Textarea(attrs={'class': 'form-control'}),
            'trabajoarealizar': forms.Textarea(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'nombre': forms.Textarea(attrs={'class': 'form-control'}),
            'telefono': forms.Textarea(attrs={'class': 'form-control'}),
        }

        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','documento','telefono','correo','ruc']
        widgets = {
            'nombre': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nombre y apellido'}),
            'documento': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Numero de documento'}),
            'telefono': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Numero de telefono'}),
            'correo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese un correo'}),
            'ruc' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ruc'}),
        }
        
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['codigo','nombre','especificacion','cantidad','precio']
        widgets = {
            'codigo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Numero de documento'}),
            'nombre': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nombre y apellido'}),
            'especificacion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ruc'}),
            'cantidad': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Numero de telefono'}),
            'precio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese un correo'}),
        }
     
     
     
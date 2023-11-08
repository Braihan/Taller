from django import forms
from .models import Tareas, Cliente


class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['trabajosolicitado', 'trabajoarealizar', 'observaciones']
        widgets = {
            'trabajosolicitado': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Trabajo solicitado por el cliente'}),
            'trabajoarealizar': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripcion'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Obsevaciones'}),
        }

        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','documento','telefono','correo','ruc']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y apellido'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de documento'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de telefono'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un correo'}),
            'ruc' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ruc'}),
        }
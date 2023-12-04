from django import forms
from .models import Tareas, Cliente


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
        
        #(label="Fecha", widget=forms.DateInput(attrs={'class': 'form-control', 'format': 'Y-m-d'})),
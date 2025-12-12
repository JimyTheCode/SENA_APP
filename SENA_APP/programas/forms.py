from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    """Formulario para crear y editar programas"""
    
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'nivel_formacion',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'descripcion',
            'competencias',
            'perfil_egreso',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
            'fecha_creacion',
        ]
        
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PROG001'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del programa'
            }),
            'nivel_formacion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'modalidad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'duracion_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en meses'
            }),
            'duracion_horas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en horas'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del programa'
            }),
            'competencias': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Competencias a desarrollar'
            }),
            'perfil_egreso': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Perfil de egreso'
            }),
            'requisitos_ingreso': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Requisitos de ingreso'
            }),
            'centro_formacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Centro de formación'
            }),
            'regional': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Regional'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fecha_creacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

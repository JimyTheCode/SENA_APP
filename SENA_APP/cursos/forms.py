from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    """Formulario para crear y editar cursos"""
    
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones',
        ]
        
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: CURS001'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del curso'
            }),
            'programa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'instructor_coordinador': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 08:00 - 12:00'
            }),
            'aula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Aula o ambiente'
            }),
            'cupos_maximos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de cupos'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observaciones del curso'
            }),
        }

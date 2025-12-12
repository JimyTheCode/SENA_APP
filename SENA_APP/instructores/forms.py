from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):
    """Formulario para crear y editar instructores con estilos visuales mejorados"""

    class Meta:
        model = Instructor
        fields = [
            'tipo_documento',
            'documento_identidad',
            'nombre',
            'apellido',
            'telefono',
            'correo',
            'fecha_nacimiento',
            'ciudad',
            'direccion',
            'nivel_educativo',
            'especialidad',
            'anos_experiencia',
            'activo',
            'fecha_vinculacion'
        ]

        # Widgets personalizados
        widgets = {
            'tipo_documento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad de residencia'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa'
            }),
            'nivel_educativo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Área de especialización'
            }),
            'anos_experiencia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Años de experiencia',
                'min': '0'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'fecha_vinculacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

        # Etiquetas personalizadas
        labels = {
            'tipo_documento': 'Tipo de Documento',
            'documento_identidad': 'Documento de Identidad',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
            'nivel_educativo': 'Nivel Educativo',
            'especialidad': 'Especialidad',
            'anos_experiencia': 'Años de Experiencia',
            'activo': 'Activo',
            'fecha_vinculacion': 'Fecha de Vinculación'
        }

    # -----------------------------
    # VALIDACIONES PERSONALIZADAS
    # -----------------------------

    def clean_documento_identidad(self):
        """Validar que el documento contenga solo números"""
        documento = self.cleaned_data.get('documento_identidad')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_telefono(self):
        """Validar que el teléfono sea numérico y tenga 10 dígitos"""
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if telefono and len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono

    def clean_anos_experiencia(self):
        """Validar que los años de experiencia sean un número positivo"""
        anos = self.cleaned_data.get('anos_experiencia')
        if anos is not None and anos < 0:
            raise forms.ValidationError("Los años de experiencia no pueden ser negativos.")
        return anos
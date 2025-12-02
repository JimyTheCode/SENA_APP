from django.db import models

# Create your models here.

class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('PAS', 'Pasaporte'),
    ]
    
    
    NIVEL_EDUCATIVO_CHOICES = [
        ('TECNICO', 'Técnico'),
        ('TGL', 'Tegnologo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especialidad'),
        ('MAE', 'Maestria'),
        ('DOC', 'Doctorado'),
    ]
    
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=200, null=True)
    nivel_educativo = models.CharField(max_length=7, choices=NIVEL_EDUCATIVO_CHOICES, default= 'MAE')
    especialidad = models.CharField(max_length=100, null=True)
    anos_experiencia = models.IntegerField(null=True)
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField(null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
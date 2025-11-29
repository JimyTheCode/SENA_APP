from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    documento_identidad = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    ciudad = models.CharField(max_length=100)
    programa = models.CharField(max_length=100)
    

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
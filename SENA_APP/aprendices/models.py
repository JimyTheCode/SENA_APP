from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    documento_identidad = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(null=True)
    ciudad = models.CharField(max_length=100 , null=True)
    programa = models.CharField(max_length=100)
    

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
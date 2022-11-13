from django.db import models

class clientes(models.Model):
      nombre = models.CharField(max_length=100)
      direccion = models.CharField(max_length=200)
      numero_dni = models.IntegerField()

def __str__(self):
      return f"{self.nombre}, {self.numero_dni}, {self.id}"

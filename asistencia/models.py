from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    uid_rfid = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.tipo} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
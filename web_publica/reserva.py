from django.db import models
from .models import GymMember

class Reserva(models.Model):
    clase = models.ForeignKey('web_publica.Clase', on_delete=models.CASCADE)
    instructor = models.ForeignKey('web_publica.Instructor', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey(GymMember, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.usuario} para la clase {self.clase}"

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class GymMember(AbstractUser):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='gym_members'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Permissions for the user'),
        related_name='gym_members'
    )

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    clase = models.ForeignKey('web_publica.Clase', on_delete=models.CASCADE)
    instructor = models.ForeignKey('web_publica.Instructor', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey(GymMember, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.usuario} para la clase {self.clase}"


class Clase(models.Model):
    # Definición de campos de la clase
    pass


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

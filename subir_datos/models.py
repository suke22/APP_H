from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Dato(models.Model):
    dia_cita = models.DateTimeField(('CITA'))
    cp = models.PositiveBigIntegerField(('CÓDIGO POSTAL'))
    direccion = models.CharField(('DIRECCIÓN'), max_length=200)
    nhc = models.CharField(('NHC'), max_length=10)
    movil = models.PositiveBigIntegerField(('MÓVIL'))
    agenda = models.CharField(('AGENDA'), max_length=30, blank = True, null = True)
    estado = models.CharField(('ESTADO'), max_length=100, blank = True, null = True)
    DNI = models.CharField(('DNI'), max_length=9, blank = True, null = True)
    incidencias = models.CharField(('INCIDENCIAS'), max_length=200,  blank = True, null = True)



    def __str__(self):
        return self.direccion
from django.db import models, connections

# Create your models here.

class Pedido(models.Model):
    DNI = models.CharField(max_length=9, blank = True, null = True)
    nhc = models.CharField(max_length=10)
    movil = models.PositiveBigIntegerField()
    cp = models.PositiveBigIntegerField()
    direccion = models.CharField(max_length=200)
    dia_cita = models.DateTimeField()
    #hora_cita = models.TimeField()

    AGENDA = [
        ("HF_FARDISP","HF_FARDISP"),
        ("HF_UPCCFAR","HF_UPCCFAR"),
        ("HF_FAR4","HF_FAR4"),
        ]
    
    agenda = models.CharField(max_length=30, choices=AGENDA, default='none')
    incidencias = models.CharField(max_length=200,  blank = True, null = True)
    
    ESTADO = [
        ("Sin revisar","Sin revisar"),
        ("Entregado","Entregado"),
        ("No entregado: Dirección erronea","No entregado: Dirección erronea"),
        ("No entregado: No hay nadie en casa","No entregado: No hay nadie en casa"),
        ]
    
    estado = models.CharField(max_length=100, choices=ESTADO,default='none')

    def __str__(self) -> str:
        return "{} ({})".format(self.direccion, self.dia_cita)

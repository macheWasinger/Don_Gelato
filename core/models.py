from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=600)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.mail, self.mensaje)
    # No hay que imprimir nada en pantalla porque los datos
    # de la persona que se contactó, tienen que archivarse
    # en la base de datos.


# Create your models here.

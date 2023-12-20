from django.db import models

# Create your models here.
class Inscritos(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=80)
    telefono= models.CharField(max_length=12)             
    fechaInscripcion = models.DateField()
    institucion = models.CharField(max_length=80)
    hora = models.TimeField()
    estado = models.CharField(max_length=60)
    observacion = models.CharField(max_length=1000, blank=True, null=True)

class Institucion(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=80)
   
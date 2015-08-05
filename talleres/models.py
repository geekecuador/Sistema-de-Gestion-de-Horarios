from django.db import models
from masterkey.models import Profesor,Sede
from masterkey.models import Estudiante
# Create your models here.
class Taller(models.Model):
    id = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=30)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    capacidad = models.IntegerField()
    profesor = models.ForeignKey(Profesor)
    lugar = models.ForeignKey(Sede)
    alumno = models.ManyToManyField(Estudiante)
    def __unicode__(self):
        return self.tema


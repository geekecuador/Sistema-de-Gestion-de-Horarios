# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.


def cedula_valida(ced):
    if len(ced) == 10:
        valores = [int(ced[x]) * (2 - x % 2) for x in range(9)]
        suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
    return int(ced[9]) == 10 - int(str(suma)[-1:])

def validacion(ced):
    if not cedula_valida(ced):
        raise ValidationError(u'%s no es un número de cédula válido' % ced)


def validar_numeros(numero):
    try:
        assert isinstance(numero, object)
        num = int(numero)
    except:
        raise ValidationError(u'%s debe ser numero' % numero)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=25)
    def __unicode__(self):
        return self.nombre
class Programa(models.Model):
    nombre_del_programa = models.CharField(max_length=25, primary_key=True)

    def __unicode__(self):
        return self.nombre_del_programa

class Sede(models.Model):
    nombre_sede = models.CharField(max_length=20,primary_key=True)
    ciudad = models.ForeignKey(Ciudad)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    def __unicode__(self):
        return self.nombre_sede

class Profesor(models.Model):
    cedula = models.CharField(u"Cédula", max_length=10, validators=[validacion])
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sede = models.ForeignKey(Sede)
    def __unicode__(self):
        return self.nombre + " "+self.apellido

class Nivel(models.Model):
    nivel =  models.CharField(max_length=2)
    def __unicode__(self):
        return self.nivel

class Estudiante(models.Model):

    cedula = models.CharField(u"cédula", max_length=10, primary_key=True, validators=[validacion])
    foto  = models.ImageField(upload_to='estudiante')
    usuario = models.OneToOneField(User,unique=True,)
    fecha_nacimiento = models.DateField(u'fecha de nacimiento',blank=True,null=True)
    telefono = models.CharField(u'teléfono',max_length=10, validators=[validar_numeros])
    direccion_dmocilio= models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)
    programa = models.ForeignKey(Programa)
    fecha_de_inicio = models.DateField()
    fecha_de_expiracion = models.DateField()
    lugar_de_trabajo = models.CharField(max_length=30)
    contacto_de_emergencia =  models.CharField(max_length=30)
    relacion_de_contacto_de_emergencia = models.CharField(max_length=30)
    telefono_de_contanto_de_emergencia = models.CharField(max_length=10)
    sede = models.ForeignKey(Sede)
    nivel = models.ForeignKey(Nivel)
    def __unicode__(self):
        return  self.cedula
class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha =  models.DateField()
    capacidad_maxima = models.PositiveSmallIntegerField()
    sede = models.OneToOneField(Sede)
    profesor =  models.ForeignKey(Profesor)
    estudiantes  =  models.ManyToManyField(Estudiante)
    max_tipo = models.PositiveIntegerField(default=3)
    tipo_estudiante = models.ManyToManyField(Nivel,related_name='tipo_estudiante', blank=True)

    def __unicode__(self):
        return str(self.hora_inicio) + " "+str(self.hora_fin) + " "+ str(self.sede) + " "+str(self.fecha)

class Taller(models.Model):
    tema = models.CharField(max_length=30)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    capacidad = models.IntegerField()
    profesor = models.ForeignKey(Profesor)
    lugar = models.OneToOneField(Sede)
    alumno = models.ManyToManyField(Estudiante)
    def __unicode__(self):
        return self.tema

class Academic_Rank(models.Model):
    curso = models.ForeignKey(Curso,blank=True);
    taller =  models.ForeignKey(Taller,blank=True);
    actividad = models.CharField(max_length=25)
    calificacion = models.CharField(max_length=2)
    profesor = models.CharField(max_length=25)
    estudiante = models.ForeignKey(Estudiante)



class Contrato(models.Model):

    numero_contrato = models.CharField(max_length=8, primary_key=True)
    numero_factura = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento',blank=True,null=True)
    cedula = models.CharField(u"Cédula", max_length=10, validators=[validacion])
    email = models.EmailField('e-mail')
    direccion_domicilio = models.TextField()
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    empresa = models.CharField(max_length=30)
    cargo = models.CharField(max_length=20)
    direccion_empresa = models.CharField(max_length=30)
    telefono_empresa = models.PositiveIntegerField()
    fecha_creacion = models.DateField(u'Fecha de creación')
    programa = models.ForeignKey(Programa)
    duracion = models.DateField()
    sede = models.ForeignKey(Sede)
    estudiante =  models.ManyToManyField(Estudiante)

    def __unicode__(self):
        return self.numero_contrato + ' ' + self.nombre + ' ' + self.apellidos


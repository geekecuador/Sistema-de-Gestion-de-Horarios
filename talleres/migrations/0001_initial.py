# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterkey', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('tema', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('capacidad', models.IntegerField()),
                ('alumno', models.ManyToManyField(to='masterkey.Estudiante')),
                ('lugar', models.ForeignKey(to='masterkey.Sede')),
                ('profesor', models.ForeignKey(to='masterkey.Profesor')),
            ],
        ),
    ]

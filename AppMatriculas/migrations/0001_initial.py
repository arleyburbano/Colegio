# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('documentoEstudiante', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('PrimerNombre', models.CharField(max_length=20)),
                ('SegundoNombre', models.CharField(max_length=20)),
                ('PrimerApellido', models.CharField(max_length=20)),
                ('SegundoApellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('sexo', models.CharField(max_length=1)),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
    ]

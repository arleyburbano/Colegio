# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMatriculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curso', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('documentoDocente', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('PrimerNombre', models.CharField(max_length=20)),
                ('SegundoNombre', models.CharField(max_length=20)),
                ('PrimerApellido', models.CharField(max_length=20)),
                ('SegundoApellido', models.CharField(max_length=20)),
                ('direccionDoc', models.CharField(max_length=50)),
                ('telefonoDoc', models.CharField(max_length=11)),
            ],
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='direccion',
            new_name='direccionEst',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='telefono',
            new_name='telefonoEst',
        ),
    ]

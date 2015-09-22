from django.db import models

class Estudiante (models.Model):
    documentoEstudiante = models.CharField(max_length=12,primary_key=True)
    PrimerNombre = models.CharField(max_length=20)
    SegundoNombre = models.CharField(max_length=20)
    PrimerApellido = models.CharField(max_length=20)
    SegundoApellido = models.CharField(max_length=20)
    direccionEst = models.CharField(max_length=50)
    telefonoEst = models.CharField(max_length=12)
    sexo = models.CharField(max_length=1)
    fechaNacimiento = models.DateField(auto_now=False)
class Docente (models.Model):
    documentoDocente = models.CharField(max_length=12,primary_key=True)
    PrimerNombre = models.CharField(max_length=20)
    SegundoNombre = models.CharField(max_length=20)
    PrimerApellido = models.CharField(max_length=20)
    SegundoApellido = models.CharField(max_length=20)
    direccionDoc = models.CharField(max_length=50)
    telefonoDoc = models.CharField(max_length=11)
class Curso (models.Model):
    curso =models.CharField(max_length=15)
    jornada =models.CharField(max_length=15)
class Materia(models.Model):
    nombreMateria =models.CharField(max_length=30)
    Curso=models.ForeignKey(Curso)
    Docente=models.ForeignKey(Docente)
class Notas(models.Model):
    Nota=models.FloatField(10)
    Estudiante=models.ForeignKey(Estudiante)
    Curso=models.ForeignKey(Curso)
    Docente=models.ForeignKey(Docente)













# Create your models here

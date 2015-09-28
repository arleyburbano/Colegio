from django.db import models

class Estudiante (models.Model):
    DocumentoEstudiante = models.CharField(max_length=12,primary_key=True)
    PrimerNombre = models.CharField(max_length=20)
    SegundoNombre = models.CharField(max_length=20)
    PrimerApellido = models.CharField(max_length=20)
    SegundoApellido = models.CharField(max_length=20)
    DireccionEst = models.CharField(max_length=50)
    TelefonoEst = models.CharField(max_length=12)
    Sexo = models.CharField(max_length=1)
    FechaNacimiento = models.DateField(auto_now=False)
class Docente (models.Model):
    DocumentoDocente = models.CharField(max_length=12,primary_key=True)
    PrimerNombre = models.CharField(max_length=20)
    SegundoNombre = models.CharField(max_length=20)
    PrimerApellido = models.CharField(max_length=20)
    SegundoApellido = models.CharField(max_length=20)
    DireccionDoc = models.CharField(max_length=50)
    TelefonoDoc = models.CharField(max_length=11)
class Curso (models.Model):
    Curso =models.CharField(max_length=15)
    Jornada =models.CharField(max_length=15)
class Materia(models.Model):
    NombreMateria =models.CharField(max_length=30)
    Curso=models.ForeignKey(Curso)
    Docente=models.ForeignKey(Docente)
class Notas(models.Model):
    Nota=models.FloatField(10)
    Estudiante=models.ForeignKey(Estudiante)
    Curso=models.ForeignKey(Curso)
    Docente=models.ForeignKey(Docente)
class IngresoUsuario(models.Model):
    Usuario=models.CharField(max_length=30)
    Contrasena=models.CharField(max_length=30)













# Create your models here

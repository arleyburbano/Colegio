
from rest_framework.serializers import ModelSerializer
from AppMatriculas.models import *

class DocenteSerializer(ModelSerializer):
    class Meta:
        model = Docente
        fields = ('DocumentoDocente','PrimerNombre','SegundoNombre','PrimerApellido','SegundoApellido','DireccionDoc','TelefonoDoc')

class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('DocumentoEstudiante','PrimerNombre','SegundoNombre','PrimerApellido','SegundoApellido','DireccionEst','TelefonoEst','Sexo','FechaNacimiento')

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','Curso','Jornada')

class MateriaSerializer(ModelSerializer):
    class Meta:
        model = Materia
        fields = ('id','NombreMateria','Curso','Docente')

class NotaSerializer(ModelSerializer):
    class Meta:
        model = Notas
        fields = ('Nota','Estudiante','Materia','Docente')

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = IngresoUsuario
        fields = ('Usuario', ('Contraseña'))




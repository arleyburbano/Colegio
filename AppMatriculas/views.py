from django.shortcuts import render
from rest_framework import generics
from AppMatriculas.Serializers import *
from AppMatriculas.models import *

class EstudianteView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class DocenteView(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class MateriaView(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class CursoView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class NotasView(generics.ListCreateAPIView):
    queryset = Notas.objects.all()
    serializer_class = NotaSerializer

class UsuarioView(generics.ListCreateAPIView):
    queryset = IngresoUsuario.objects.all()
    serializer_class = UsuarioSerializer

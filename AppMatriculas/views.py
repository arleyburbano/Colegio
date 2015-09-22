from django.shortcuts import render
from rest_framework import generics
from AppMatriculas.Serializers import *
from AppMatriculas.models import *

class EstudianteView(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


# Create your views here.

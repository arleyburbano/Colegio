"""Colegio1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from AppMatriculas.views import *
#from django.contrib import admin

#admin.autodiscover()

#urlpatterns = patterns('',
   # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   # url(r'^admin/', include(admin.site.urls)))

urlpatterns = [
    url(r'^usuario/$',UsuarioView.as_view(),name='IngresoUsuario'),
]

urlpatterns = [
    url(r'^estudiante/$',EstudianteView.as_view(),name='Estudiante'),
]
urlpatterns = [
    url(r'^docente/$',DocenteView.as_view(),name='Docente'),
]
urlpatterns = [
    url(r'^materia/$',MateriaView.as_view(),name='Materia'),
]
urlpatterns = [
    url(r'^curso/$',CursoView.as_view(),name='Curso'),
]
urlpatterns = [
    url(r'^notas/$',NotasView.as_view(),name='Notas'),
]
from django.template import Template, Context, loader
from django.shortcuts import render

def Index(recuest):
    return render(recuest,"Index.html")

def Proyectos(recuest):
    return render(recuest,"Proyectos.html")

def Habilidades(recuest):
    return render(recuest,"Habilidades.html")

def Contacto(recuest):
    return render(recuest,"Contacto.html")


from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Soy Luis - Hola Django - Coder")

def segundaVista(request):

    return HttpResponse("<br><br>---------YA SOMOS PROGRAMADORES-----------")


def dia (request):

    variable = datetime.now()

    return HttpResponse(f"Hoy es un gran dia<br> {variable}")

def apellido(request,ape):

    fecha = datetime.now()

    return HttpResponse(f"El profe de coder {ape}, es muy bueno..<br><br>..- Por lo menos hoy:{fecha}")

def probandoTemplate(request):

    miHTML = open("C:/Users/luis_/Desktop/Proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")

    plantilla = Template(miHTML.read())

    miHTML.close()

    miCOntexto = Context()

    documento = plantilla.render(miCOntexto)

    return HttpResponse(documento)
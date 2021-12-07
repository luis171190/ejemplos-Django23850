from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

#Paso 1
from django.template import loader

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
    
    mejorEstudiante = "Ilan Fritzler"
    
    nota = 8.9
    
    fecha = datetime.now()
    
    estudianteMasSimpaticos = ["Juanse","Nadia","Cristo","Laura"]
    
    dicc = {"nombre":mejorEstudiante, "nota":nota, "fecha":fecha, "estudiantes":estudianteMasSimpaticos}
    
    #Paso 3
    plantilla = loader.get_template("template1.html")

    #miHTML = open("C:/Users/luis_/Desktop/Proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")

    #plantilla = Template(miHTML.read())

    #miHTML.close()

    #miCOntexto = Context(dicc)

    #documento = plantilla.render(miCOntexto)

    documento = plantilla.render(dicc)

    return HttpResponse(documento)
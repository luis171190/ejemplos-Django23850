from django.shortcuts import render

from django.shortcuts import HttpResponse

from AppCoder.models import Estadio, Equipo
from AppCoder.forms import EstadioFormulario


def busquedaEquipo(request):
    
    return render(request, "AppCoder/busquedaEquipo.html")

def buscar(request):
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        ciudad = Equipo.objects.filter(nombre_incontains=nombre)
        
               
        #respuesta = f"Estoy Buscando a : {request.GET['nombre']} "
        
        return render(request, "AppCoder/resultadoBusqueda.html" )
        
        
    else:
        
        repuesta = "Che, mandame informacion!!"
    
    return HttpResponse(respuesta)



# Create your views here.

def estadioFormulario(request):
    
    #Obtiene la direccion y el anioFund
    
    if request.method == "POST":
        
        miFormulario = EstadioFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
        
            estadioInsta = Estadio(direccion=informacion["direccion"] , anioFund=informacion["anioFund"])
            
            estadioInsta.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    else:
        
        miFormulario = EstadioFormulario()
    #return HttpResponse("Esto de es una prueba del inicio")
    
    return render(request, 'AppCoder/estadioFormulario.html',{"miFormulario":miFormulario})


#Primer Vista
def inicio(request):
    
    #return HttpResponse("Esto de es una prueba del inicio")
    
    return render(request, 'AppCoder/inicio.html')

def equipos(request):
    
    
    return render(request, 'AppCoder/equipos.html')

def jugadores(request):
    
    
    return render(request, 'AppCoder/jugadores.html')
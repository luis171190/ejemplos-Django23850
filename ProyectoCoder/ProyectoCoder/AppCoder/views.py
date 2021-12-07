from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

#Primer Vista
def inicio(request):
    
    #return HttpResponse("Esto de es una prueba del inicio")
    
    return render(request, 'AppCoder/inicio.html')
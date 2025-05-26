from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo desde Fireploy Django!")

def home_view(request):
    context = {
        'title': 'Bienvenido a Fireploy',
        'mensaje': 'Template oficial de Fireploy en Django',
    }
    return render(request, 'fireploy/home.html', context)
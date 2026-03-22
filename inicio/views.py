from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Página de inicio")
def nosotros(request):
    return HttpResponse("Página sobre nosotros")
def contacto(request):
    return HttpResponse("Página de contacto")

# Create your views here.

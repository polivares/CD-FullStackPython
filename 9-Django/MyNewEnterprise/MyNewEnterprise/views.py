# MyNewEnterprise/views.py

from django.shortcuts import HttpResponse

# Funciones para el manejo de vistas

def index(request):
    return HttpResponse('<h1>Bienvenido a MyEnterprise s.a.</h1>')

def search(request):
    return HttpResponse('<h1>Búsqueda</h1>')
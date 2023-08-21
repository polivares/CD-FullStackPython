# App1/views.py
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    context = {
        'nombre': 'Optimus Prime',
        'pos_cargo': 1,
        'amigos': ['Bumblebee', 'Ratchet', 'Ironhide']
    }
    # Se crea la variable de sesión con un nombre
    request.session['nombre'] = context['nombre']
    return render(request, 'index.html', context)


def solicitudes(request):
    # Si variable de sesión no fue creada, se redirige tráfico a index de app1
    context = {
        'nombre': request.session.get("nombre")
    }
    if request.session.get("nombre") == None:
        return redirect("/app1")
    elif request.method == "POST":
        print("Se detectó una solicitud POST")
        print(request.POST)
        context['solicitud'] = 'POST'
    return render(request, "solicitudes.html", context)


def form(request):
    # Si variable de sesión no fue creada, se redirige tráfico a index de app1
    if request.session.get("nombre") == None:
        return redirect("/app1")
    context = {
        'nombre': request.session.get("nombre")
    }
    return render(request, "form.html", context)

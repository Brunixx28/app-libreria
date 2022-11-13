from django.shortcuts import render
from libreria.models import clientes

def index(request):
    return render(request, "libreria/saludar.html")

def numero_lista(request):
   return render(request, "libreria/saludar.html",
    {"listas": [1,2,3,4,5,6,7,8,9]}
    )

def monstrar_clientes(request):
  lista_clientes = clientes.objects.all()
  return render(request, "libreria/clientes.html",
                {"lista_clientes": lista_clientes})
   
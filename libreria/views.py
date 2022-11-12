from django.shortcuts import render

def index(request):
    return render(request, "libreria/saludar.html")

def numero_lista(request):
    return render(request, "libreria/saludar.html",
    {"listas": [1,2,3,4,5,6,7,8,9]}
    )

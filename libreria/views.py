from django.shortcuts import render
from libreria.models import clientes
from libreria.forms import Buscar, libreriaForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

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

class Buscarclientes(View):

    form_class = Buscar
    template_name = 'libreria/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_clientes = clientes.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_clientes':lista_clientes})
        return render(request, self.template_name, {"form": form})

class AltaCliente(View):

    form_class = libreriaForm
    template_name = 'libreria/alta_cliente.html'
    initial = {"nombre":"", "direccion":"", "numero_dni":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el cliente {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
        
            
class ClientesList(ListView):
    model = clientes

class ClientesCrear(CreateView):
    model = clientes
    success_url = "/panel-cliente"
    fields = ["nombre", "direccion", "numero_dni"]

class ClientesBorrar(DeleteView):
    model = clientes
    success_url = "/panel-cliente"

class ClientesActualizar(UpdateView):
    model = clientes
    success_url = "/panel-cliente"
    fields = ["nombre", "direccion"]
   
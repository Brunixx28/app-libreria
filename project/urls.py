"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from libreria.views import (index, numero_lista, monstrar_clientes, Buscarclientes,
                        AltaCliente, ClientesList, ClientesCrear, ClientesBorrar, ClientesActualizar)
from blog.views import index as blog_index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", index),
    path("lista/", numero_lista),
    path("mis-clientes/", monstrar_clientes),
    path('blog/', blog_index),
    path("mi-cliente/buscar", Buscarclientes.as_view()),
    path("mi-cliente/alta", AltaCliente.as_view()),
    path("panel-cliente/", ClientesList.as_view()), 
    path("panel-cliente/crear", ClientesCrear.as_view()),
    path("panel-cliente/<int:pk>/borrar", ClientesBorrar.as_view()),
    path("panel-cliente/<int:pk>/actualizar", ClientesActualizar.as_view()),
    path('blog/', include('blog.urls')),
]


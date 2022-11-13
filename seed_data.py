from libreria.models import clientes

clientes(nombre="Felipe", direccion="Grecia 35", numero_dni=653421).save()
clientes(nombre="Liliana", direccion="Rivadavia 954", numero_dni=653907).save()
clientes(nombre="Dardo", direccion="Ituzango 912", numero_dni=698521).save()
clientes(nombre="Emanuele", direccion="Italia Azul 906", numero_dni=128521).save()
clientes(nombre="Elias", direccion="Neuquen 09", numero_dni=338521).save()


print("se cargo con exito")

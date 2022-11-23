from libreria.models import clientes

clientes(nombre="Felipe", direccion="Grecia 35", numero_dni=653421).save()
clientes(nombre="Liliana", direccion="Rivadavia 954", numero_dni=653907).save()
clientes(nombre="Dardo", direccion="Ituzango 912", numero_dni=698521).save()
clientes(nombre="Emanuele", direccion="Italia Azul 906", numero_dni=128521).save()
clientes(nombre="Elias", direccion="Neuquen 09", numero_dni=338521).save()


print("se cargo con exito")

from blog.models import Post

Post(title="Mi post", short_content="un post", content="si todo sale bien este mensaje les va a salir a todos, Vanesa volveee").save()


print("Se cargo con exito en la libreria")

from django.contrib import admin
from blog.models import Post
from libreria.models import clientes

admin.site.register(clientes)

admin.site.register(Post)

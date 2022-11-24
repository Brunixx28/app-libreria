from django.db import models   

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateField(auto_now_add=True)
    

def __str__(self):
    return f"id:{self.id}, title:{self.title}"

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    
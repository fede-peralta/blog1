from django.db import models
from django.utils import timezone


# Create your models here. clase Categoria

class Categoria(models.Model):
    nombre=models.CharField( max_length=50, null=False)
    
    
    def __str__(self):
        return self.nombre


class Noticias(models.Model):
    titulo =  models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/noticia_default.png')
    publicado = models.DateTimeField(default=timezone.now)



    class Meta:  # orden as-ds
        ordering = ('-publicado',)
        
    
    def __str__(self):
        return self.titulo

    
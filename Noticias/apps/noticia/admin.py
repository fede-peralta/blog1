from django.contrib import admin
from .models import Noticias, Categoria


# Register your models here.
@admin.register(Noticias)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')
    

    admin.site.register(Categoria)
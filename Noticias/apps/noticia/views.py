from django.views.generic import ListView, DetailView
from.models import Noticias

#from apps.noticia.views import noticia --->  problema de importacin circular


# Create your views here.

class NoticiasListView(ListView):
    model = Noticias
    template_name = "posts/noticias.html"
    context_object_name = "noticias"
    

class NoticiasDetailView(DetailView):
    model = Noticias
    template_name = "posts/noticias_individual.html"
    context_object_name = "noticias"
    pk_url_kwarg = "id"
    queryset = Noticias.objects.all()
    
from django.urls import path
from .views import NoticiasDetailView, NoticiasListView

app_name = 'apps.noticia'


urlpatterns = [
    path('noticia/',NoticiasListView.as_view(), name='noticia'),
    path("noticas/<int:id>/", NoticiasDetailView.as_view(), name = "noticias_individual"),
]
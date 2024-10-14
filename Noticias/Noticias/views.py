from django.views.generic import TemplateView


class IndexView(TemplateView):
    
    template_name='index.html'
    

class NoticiasView(TemplateView):
    
    template_name='noticias.html'
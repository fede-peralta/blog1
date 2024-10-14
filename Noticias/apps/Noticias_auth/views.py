from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import views as auth_vews

from Noticias.apps.Noticias_auth.forms import SingUpForm



# Create your views here.

class SingUpView(FormView):
    template_name = "registration/register.html"
    form_class = SingUpForm
    success_url = reverse_lazy("apps.blog_auth:login")
    
    
    def form_valid(self, form):
        "verificamos que los datos sean validos y lo guardamos"
        form.save()
        return super().form_valid(form)

class Login(auth_vews.LoginView):
    template_name = "registrarion/login.html"
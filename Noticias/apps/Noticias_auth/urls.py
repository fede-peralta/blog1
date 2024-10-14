from django.urls import path
from. views import SinUpView
from django.contrib.auth import views as auth_views


app_name = "apps.noticias_auth"

urlpatterns = [
    path("register/", SinUpView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(), name = "login")
    
]

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Noticias.apps.Noticias_auth.models import Eventos

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['titulo', 'descripcion', 'fecha', 'ubicacion']
        widgets ={
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
        
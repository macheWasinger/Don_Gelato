from django import forms
from django.forms import ModelForm
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'mail', 'mensaje']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
from django import forms

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label = 'Email')
    username = forms.CharField(label='Username')
    #cc_myself = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]

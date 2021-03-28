from django import forms

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label = 'Email')
    username = forms.CharField(label='Username')
    #cc_myself = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

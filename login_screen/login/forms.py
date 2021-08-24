from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'password')

from django.shortcuts import render

from .models import LoginModel


def login_page(request):
    """View function for home page of site."""
    username = LoginModel.username
    password = LoginModel.password

    context = {
        'Enter a username': username,
        'Enter a password': password,
    }

    return render(request, 'login.html', context=context)


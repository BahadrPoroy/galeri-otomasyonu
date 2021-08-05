from django.shortcuts import render

from .models import LoggedModel


def logged(request):
    """View function for home page of site."""
    text = LoggedModel.text

    context = {
        "You are logged in": text,
    }

    return render(request, 'logged.html', context=context)


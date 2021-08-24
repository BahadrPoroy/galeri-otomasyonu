from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, SigninForm
from django.contrib.auth import authenticate, login


def SigninView(request):
    form = SigninForm()
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = form.cleaned_data["username"]
            messages.error(request, 'User successfully created')
            return redirect("http://127.0.0.1:8000/login")
    else:
        form = SigninForm()
    return render(request, "signin.html", {'form': form})


def LoginView(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:8000/login/logged")
            else:
                messages.error(request, 'username or password not correct')
                return redirect("http://127.0.0.1:8000/login")
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})

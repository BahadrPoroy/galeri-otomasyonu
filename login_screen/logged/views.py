from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages


@login_required(login_url="http://127.0.0.1:8000/login")
def loggedview(request):
    return render(request, "logged.html")


@login_required(login_url="http://127.0.0.1:8000/login")
def logoutview(request):
    logout(request)
    messages.error(request, 'You are logged out')
    return render(request, "logout.html")


@login_required(login_url="http://127.0.0.1:8000/login")
def usermanagementview(request):
    users = User.objects.order_by("-username")
    return render(request, "users.html", {"users": users})


@login_required(login_url="http://127.0.0.1:8000/login")
def userchangeview(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, "userchange.html", {"user": user})

@login_required(login_url="http://127.0.0.1:8000/login")
def userdeleteview(request, pk, *args, **kwargs):
    user = User.objects.get(pk=pk)
    User.objects.filter(pk=pk).delete()
    return render(request, "delete.html", {"user": user})

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name="loginView"),
    path('signin/', views.SigninView, name="SigninView"),
]
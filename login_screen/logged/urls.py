from django.urls import path
from . import views

urlpatterns = [
    path('login/logged/', views.loggedview, name='loggedview'),
    path('logged/logout/', views.logoutview, name='logoutview'),
    path('users/', views.usermanagementview, name="usermanagementview"),
    path('users/<int:pk>/change/', views.userchangeview, name='userchangeview'),
    path('users/<int:pk>/delete/', views.userdeleteview, name="delete_user"),
]

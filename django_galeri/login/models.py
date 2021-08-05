from django.db import models


class LoginModel(models.Model):

    username = models.CharField(max_length=20, help_text='Enter your username')
    password = models.CharField(max_length=20, help_text='Enter your password')


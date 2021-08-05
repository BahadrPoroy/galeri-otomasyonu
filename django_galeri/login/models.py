from django.db import models


class LoginModel(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    username = models.CharField(max_length=20, help_text='Enter your username')
    password = models.CharField(max_length=20, help_text='Enter your password')

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
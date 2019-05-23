from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

# users = User.objects.all()

class CustomUser(AbstractUser):
    alias = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)


from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager

class User(AbstractUser):
    username = models.CharField(max_length=100, unique = True)
    email = models.EmailField(unique=True)
    is_librarian = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    
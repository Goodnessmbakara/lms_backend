from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager

class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)

    
    
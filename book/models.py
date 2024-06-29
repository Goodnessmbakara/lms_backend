from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} by '{self.author}' ({self.quantity})"
    
class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user} - {self.book}'

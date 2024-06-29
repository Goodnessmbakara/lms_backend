from rest_framework import serializers
from .models import Book, Borrowing
from user.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'quantity', 'available']

class BorrowingSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    
    class Meta:
        model = Borrowing
        fields = ['id', 'user', 'book', 'borrowed_at', 'returned_at']
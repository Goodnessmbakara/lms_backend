# api/views.py
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import IsLibrarian
from .serializers import BookSerializer, BorrowingSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsLibrarian]
        else:
            permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['available']
    search_fields = ['title', 'author', 'genre']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsLibrarian]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class ReturnBookView(generics.UpdateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        borrowing = self.get_object()
        if borrowing.user != request.user:
            return Response({'error': 'You did not borrow this book.'}, status=status.HTTP_403_FORBIDDEN)
        borrowing.returned_at = timezone.now()
        borrowing.book.available = True
        borrowing.book.save()
        borrowing.save()
        return Response({'status': 'book returned'}, status=status.HTTP_200_OK)

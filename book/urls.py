# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  BookViewSet, BorrowBookView, ReturnBookView

router = DefaultRouter()
router.register(r'', BookViewSet)

urlpatterns = [
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:id>/', ReturnBookView.as_view(), name='return-book'),
    path('', include(router.urls)),
]

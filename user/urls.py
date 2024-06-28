
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import UserCreateView, UserListView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

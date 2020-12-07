from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from client import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('current/', views.MyTokenObtainPairView.as_view()),
    path('signup/', views.MyTokenObtainPairView.as_view())
]
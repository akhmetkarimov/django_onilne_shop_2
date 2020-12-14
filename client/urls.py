from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from client import views

from rest_framework import routers

router = routers.DefaultRouter()

# router.register(r'currentTest/',  views.UserViewSet,  basename='current')
router.register(r'test',  views.UserViewSetModel,  basename='test')

# urlpatterns = [
#     path('token/', TokenObtainPairView.as_view()),
#     path('token/refresh/', TokenRefreshView.as_view()),
#     path('current/', views.UserViewSet.as_view({'get':'retrieve'})),
# ]

# router.register(r'signup/',  views.UserViewSet,  basename='signup')

urlpatterns = router.urls



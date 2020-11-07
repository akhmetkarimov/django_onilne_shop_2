from django.urls import path
from product import views

urlpatterns = [
    path('characteristic/', views.CharacteristicViews.as_view()),
    path('characteristic/<int:pk>', views.CharacteristicDetailViews.as_view()),
    path('category/', views.CategoryViews.as_view()),
    path('product/', views.ProductViews.as_view()),
]

from django.urls import path
from order import views

urlpatterns = [
    path('order_basket/', views.OrderBasketViews.as_view()),
    # path('order/', ),
]

from django.urls import path
from product import views
from rest_framework import routers
router = routers.DefaultRouter()


characteristic_view = views.CharacteristicViewSet.as_view({'get':'list'})
characteristic_detail = views.CharacteristicViewSet.as_view({'get':'retrieve'})

router.register(r'characteristicRouter',  views.CharacteristicViewSet,  basename='characteristic')

urlpatterns = [
    path('characteristic/', views.CharacteristicViews.as_view()),
    # path('characteristicViewSet/', characteristic_view),
    path('characteristicViewSet/<int:pk>', characteristic_detail),
    path('characteristic/<int:pk>', views.CharacteristicDetailViews.as_view()),
    path('category/', views.CategoryViews.as_view()),
    path('product/', views.ProductViews.as_view()),
    path('test123/', views.testFunction)
]

urlpatterns += router.urls

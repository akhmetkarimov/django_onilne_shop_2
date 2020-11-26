from rest_framework import serializers
from order import models
from product import serializers as product_serializers


class OrderBasketSerializersPost(serializers.ModelSerializer):
    class Meta:
        model = models.OrderBasket
        fields = ('id', 'product', 'quantity')

class OrderBasketSerializersGet(serializers.ModelSerializer):
    product = product_serializers.ProductSerializers()
    class Meta:
        model = models.OrderBasket
        fields = ('id', 'product', 'quantity')
    

# class OrderSerializersPost(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = ('id', 'order', 'user')

# class OrderSerializersGet(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = ('id', 'order', 'user')

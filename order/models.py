from django.db import models
from client import models as user_models
from product import models as product_models
from basket import models as basket_models
import datetime

class OrderBasket(models.Model):
    product = models.ForeignKey(product_models.Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    is_order = models.BooleanField(default=False)



class Order(models.Model):
    user = models.ForeignKey(user_models.BaseUser, on_delete=models.CASCADE)
    order = models.ManyToManyField(OrderBasket, related_name="items")
    total = models.PositiveIntegerField(null=True, blank=True)


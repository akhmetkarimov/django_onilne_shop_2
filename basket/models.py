from django.db import models
from client import models as user_models
from product import models as product_models
# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(user_models.BaseUser, on_delete=models.CASCADE)
    product = models.ForeignKey(product_models.Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    time = models.DateTimeField(default='', auto_now=False, auto_now_add=False)
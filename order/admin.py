from django.contrib import admin
from order import models
# Register your models here.

admin.site.register(models.OrderBasket)
admin.site.register(models.Order)
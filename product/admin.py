from django.contrib import admin
from mptt import admin as mptt_admin
from product import models


class CategoryAdmin(mptt_admin.DraggableMPTTAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal=('categories', )


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Characteristic)
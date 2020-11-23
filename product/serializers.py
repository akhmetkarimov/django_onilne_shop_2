from rest_framework import serializers
from product import models


class RecursiveSerializers(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CharacteristicSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Characteristic
        fields = ('id', 'manufacturer', 'weight', 'color', 'model')


class CategorySerializers(serializers.ModelSerializer):
    children = RecursiveSerializers(many=True)

    class Meta:
        model = models.Category
        fields = ('id', 'category_name', 'parent', 'children')



class CategoryForProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'category_name')


class ProductSerializers(serializers.ModelSerializer):
    # characteristic = CharacteristicSerializers
    # categories = CategoryForProductSerializers(many=True)

    class Meta:
        model = models.Product
        fields = '__all__'


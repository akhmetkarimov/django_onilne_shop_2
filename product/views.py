from rest_framework.response import Response
from rest_framework.views import APIView
from product import serializers, models


class CharacteristicViews(APIView):
    serializers_classes = serializers.CharacteristicSerializers

    def get(self, request):
        characteristics = models.Characteristic.objects.all()
        serializer_elem = self.serializers_classes(characteristics, many=True)
        return Response(serializer_elem.data)

    def post(self, request):
        element = request.data
        serializer_elem = self.serializers_classes(data=element)
        
        if serializer_elem.is_valid():
            serializer_elem.save()
            return Response(serializer_elem.data)
        
        return Response({"status": "faild", "message": serializer_elem.errors})


class CategoryViews(APIView):
    serializers_classes = serializers.CategorySerializers

    def get(self, request):
        categories = models.Category.objects.filter(parent=None)
        serializer_elem = self.serializers_classes(categories, many=True)
        return Response(serializer_elem.data)


class ProductViews(APIView):
    serializers_classes = serializers.ProductSerializers

    def get(self, request):
        products = models.Product.objects.all()
        serializer_elem = self.serializers_classes(products, many=True)
        return Response(serializer_elem.data)



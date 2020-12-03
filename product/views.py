from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from product import serializers, models
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.http import HttpResponse
from rest_framework import permissions



from product import utils

class ProductViews(ListAPIView):
    serializer_class = serializers.ProductSerializers
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # pagination_class = utils.BaseProductPagination
    ordering_fields = ['product_price', 'product_sale']
    search_fields = ['product_name', 'product_description']
    filterset_fields = ['product_price', 'product_sale', 'is_feachered']


class CharacteristicViews(APIView):
    permission_classes = (permissions.IsAuthenticated, )
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

class CharacteristicDetailViews(APIView):
    serializers_classes = serializers.CharacteristicSerializers

    def get_queryset(self, pk):
        element = None
        try:
            element = models.Characteristic.objects.get(pk=pk)
        except models.Characteristic.DoesNotExist:
            return False
        return element

    def get(self, request, pk):
        item = self.get_queryset(pk)
        
        if not item:
            return Response({"message": "NOT FOUND"})
        
        serialized_item  = self.serializers_classes(item)
        return Response(serialized_item.data)


    def delete(self, request, pk):
        item = self.get_queryset(pk)
        
        if not item:
            return Response({"message": "NOT FOUND"})
        
        item.delete()
        return Response({"message":"DELETED"})


    def put(self, request, pk):
        item = self.get_queryset(pk)
        if not item:
            return Response({"message": "NOT FOUND"})
            
        serialized_item = self.serializers_classes(item, data=request.data)
        
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        else:
            return Response({"message": serialized_item.errors})



class CategoryViews(APIView):
    serializers_classes = serializers.CategorySerializers

    def get(self, request):
        categories = models.Category.objects.filter(parent=None)
        serializer_elem = self.serializers_classes(categories, many=True)
        return Response(serializer_elem.data)


# class ProductViews(APIView):
#     serializers_classes = serializers.ProductSerializers

#     def get(self, request):
#         products = models.Product.objects.all()
#         serializer_elem = self.serializers_classes(products, many=True)
#         return Response(serializer_elem.data)


#     def post(self, request):
#         element = request.data
#         serializer_elem = self.serializers_classes(data=element)
        
#         if serializer_elem.is_valid():
#             serializer_elem.save()
#             return Response(serializer_elem.data)
        
#         return Response({"status": "faild", "message": serializer_elem.errors})


def testFunction(request):
    return HttpResponse('HELLO TEST 123')
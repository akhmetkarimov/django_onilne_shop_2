from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from order import serializers, models
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.http import HttpResponse


class OrderBasketViews(APIView):

    def get(self, request):
        characteristics = models.OrderBasket.objects.all()
        serializer_elem = serializers.OrderBasketSerializersGet(characteristics, many=True)
        
        totalSum = 0

        for item in serializer_elem.data:
            totalSum += item['product']['product_price'] * item['quantity']


        result = {
            'all': serializer_elem.data,
            'total': totalSum
        }

        return Response(result)

    def post(self, request):
        element = request.data
        serializer_elem = serializers.OrderBasketSerializersPost(data=element)
        
        if serializer_elem.is_valid():
            serializer_elem.save()
            return Response(serializer_elem.data)
        
        return Response({"status": "faild", "message": serializer_elem.errors})
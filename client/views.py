from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from client import serializers
from client import models

from rest_framework.decorators import action
from rest_framework import viewsets



class UserViewSet(viewsets.ViewSet):

    # @action(methods=['get'], detail=True, url_path='current', url_name='currents')
    def retrieve(self, request):
        serializer = serializers.ClientSerializer(request.user)
        return Response(serializer.data)


    # @action(methods=['post'], detail=True, url_path='signup', url_name='signup')
    # def create(self, request):
    #     user = request.data
    #     new_user = models.BaseUser(username=user['username'])
    #     new_user.set_password(user['password'])
    #     new_user.save()
    #     return Response({"status": "created"})



class UserViewSetModel(viewsets.ModelViewSet):
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.ClientSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from client import serializers
from client import models


class MyTokenObtainPairView(APIView):
    serializer_class = serializers.ClientSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def post(self, request):
        user = request.data
        new_user = models.BaseUser(username=user['username'])
        new_user.set_password(user['password'])
        new_user.save()
        return Response({"status": "created"})

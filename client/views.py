from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from client import serializers


class MyTokenObtainPairView(APIView):
    serializer_class = serializers.ClientSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
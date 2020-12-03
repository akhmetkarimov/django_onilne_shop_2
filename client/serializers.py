from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from client import models


# class ClientSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['id'] = user.id
#         token['phone_number'] = user.phone_number
#         token['email'] = user.email

#         return token

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseUser
        fields = ('id', 'email', 'phone_number')


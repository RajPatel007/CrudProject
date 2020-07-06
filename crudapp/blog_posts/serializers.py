from rest_framework import serializers
from .models import UserApis


class UserApisSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)

    def create(self, validate_data):
        return UserApis.objects.create(**validate_data)

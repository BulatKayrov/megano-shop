from django.contrib.auth.models import User
from rest_framework import serializers

from profile_app.models import Profile


class SingUpSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Регистрация пользователя и создание профиля
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['name']
        )
        Profile.objects.create(fullName=validated_data['name'], user=user)
        return user

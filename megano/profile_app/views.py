from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from typing import Any
from .models import Profile
from .serializers import ProfileSerializers, ProfilePasswordSerializers, ProfileAvatarSerializers


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializers

    def get_object(self) -> Any:
        """
        Получает и возвращает Profile пользователя
        """
        return self.request.user.profile

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Получает Profile пользователя
        """

        queryset = self.get_queryset().get(user__username=request.user.username)
        serializers = ProfileSerializers(queryset)
        return Response(serializers.data)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        бновляет Profile пользователя
        """

        return super().update(request, *args, **kwargs)


class ProfilePasswordAPIview(APIView):
    """
    API представление для изменения пароля пользователя.
    После успешной проверки пользователя через сериализатор,
    изменяет пароль на новый.
    """

    def post(self, request: Request) -> Response:
        serializers = ProfilePasswordSerializers(data=request.data)
        if serializers.is_valid():
            user = User.objects.get(username=request.user.username)
            user.set_password(raw_password=request.data['newPassword'])
            user.save()
            return Response(status=200)


class ProfileAvatarAPIView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializers

    def get_object(self) -> Any:
        """
        Получает и возвращает Profile пользователя
        """
        return self.request.user.profile

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Обновляет профайл пользователя
        """
        return super().update(request, *args, **kwargs)

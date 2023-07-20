from django.shortcuts import render

import json

from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_app.serializers import SingUpSerializers
import logging

log = logging.getLogger(__name__)


class SingInAPIView(APIView):
    """Login users"""
    def post(self, request):
        """Получаем данные и сразу проверяем что user есть и выполняем вход в систему"""
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            log.info(f'sign-in {username}')
            return Response(status=200)
        return Response(status=500)


class SingUpAPIView(APIView):
    """Registrations users"""
    def post(self, request):
        """Принимием данные и проверяем на валидность, после создание юзера, осуществляем вход в систему"""
        data = json.loads(request.body)
        serializers = SingUpSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)
            # Наверное не имеет смысла проверять, так как мы его регистрируем ???
            if user:
                login(request, user)
                log.info('sign-up', username)
                return Response(status=200)
        return Response(status=500)


class SingOutAPIView(APIView):
    """logout users"""
    def post(self, request):
        logout(request)
        return Response(status=200)



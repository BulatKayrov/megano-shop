from django.urls import path
from .views import (
    SingInAPIView,
    SingOutAPIView,
    SingUpAPIView,
)

app_name = 'auth_app'

urlpatterns = [
    path('api/sign-in', SingInAPIView.as_view()),
    path('api/sign-out', SingOutAPIView.as_view()),
    path('api/sign-up', SingUpAPIView.as_view()),
]

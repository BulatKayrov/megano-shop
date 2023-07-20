from django.urls import path
from .views import ProfileAPIView, ProfilePasswordAPIview, ProfileAvatarAPIView

app_name = 'profile_app'

urlpatterns = [
    path('api/profile', ProfileAPIView.as_view()),
    path('api/profile/password', ProfilePasswordAPIview.as_view()),
    path('api/profile/avatar', ProfileAvatarAPIView.as_view()),
]


from django.urls import path
from .views import TagsAPIView
from django.views.decorators.cache import cache_page

app_name = 'tags'

urlpatterns = [
    path('api/tags/', cache_page(60*5)(TagsAPIView.as_view())),
]


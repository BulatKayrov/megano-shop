from rest_framework import generics
from .models import Tags
from .serializers import TagsSerializers


class TagsAPIView(generics.ListAPIView):
    """Теги"""
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers

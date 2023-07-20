from rest_framework import serializers

from .models import Tags


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
        depth = 1

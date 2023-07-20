from rest_framework import serializers

from profile_app.models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['fullName', 'email', 'phone', 'avatar']

    def get_avatar(self, obj):
        if obj.avatar:
            return {'src': obj.avatar.url, 'alt': obj.avatar.name}
        return None


class ProfilePasswordSerializers(serializers.Serializer):
    currentPassword = serializers.CharField(max_length=255)
    newPassword = serializers.CharField(max_length=255)


class ProfileAvatarSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['avatar']

from .models import CustomUser
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CustomUserSerializer(UserDetailsSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, user):
        request = self.context.get('request')
        image_url, image_thumbnail_url = user.image_url(request)
        return image_url

    image_thumbnail = serializers.SerializerMethodField()

    def get_image_thumbnail(self, user):
        request = self.context.get('request')
        image_url, image_thumbnail_url = user.image_url(request)
        return image_thumbnail_url

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'github_account', 'image', 'image_thumbnail', 'date_joined', 'language', 'is_active', 'last_login', 'is_staff', 'is_superuser',)

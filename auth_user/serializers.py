from .models import CustomUser
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from PIL import Image
from io import BytesIO
import base64

class CustomUserSerializer(UserDetailsSerializer):        
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'github_account', 'image', 'image_thumbnail', 'date_joined', 'language', 'is_active', 'last_login', 'is_staff', 'is_superuser',)

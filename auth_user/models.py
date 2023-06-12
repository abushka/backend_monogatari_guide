from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django_resized import ResizedImageField
import uuid
import datetime

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The username must be set")

        user = self.model(username=username, date_joined=datetime.now())
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.date_joined = datetime.now()
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=False, null=True, blank=True)
    github_account = models.URLField(blank=True, null=True)
    image = ResizedImageField(default='', size=[512, 512], quality=100, upload_to='profile_pictures/', blank=True)
    date_joined = models.DateTimeField(null=True, default=None)
    LANGUAGE_CHOICES = (
        ('ru', 'Russian'),
        ('en', 'English'),
    )
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    def image_url(self, request):
        if self.image != '':
            return request.scheme + '://' + request.get_host() + str(self.image.url)
        else:
            return None

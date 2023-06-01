from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
import uuid

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The username must be set")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=False, null=True)
    github_account = models.URLField(blank=True, null=True)
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

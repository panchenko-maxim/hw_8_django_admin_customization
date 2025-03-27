from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, nickname, password=None, **extra_fields):
        if not nickname:
            raise ValueError('Nickname field required')
        user = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nickname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(nickname, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=100, unique=True, verbose_name='nickname')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='first_name')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, verbose_name='email')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Date of registration')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        # permissions = [
        #     ("can_view_profiles", "Can watch profiles another users"),
        #     ("can_edit_profiles", "Can edit profiles another users"),
        # ]

    def __str__(self):
        return self.nickname

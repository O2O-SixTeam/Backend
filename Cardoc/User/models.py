from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            token = Token.objects.create(user=instance)
            print(token)

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Give me Email')
        user = self.model(email=email, password=password, **extra_fields)

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active',True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


GENDER_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, null=True, blank=True, max_length=10)
    email = models.EmailField(max_length=50, unique=True)
    birth = models.DateField(null=True, blank=True)
    CustomID = models.CharField(max_length=15, null=True, blank=True, unique=True)
    password = models.CharField(max_length=20, null=True, blank=True)

    is_staff = models.BooleanField(default=False, blank=True)

    USERNAME_FIELD = 'CustomID'
    REQUIRED_FIELDS = ['name', 'phone', 'gender', 'birth', 'email']

    objects = CustomUserManager()

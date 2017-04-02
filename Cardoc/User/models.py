from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from Cardoc import settings

GENDER_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUserManager(BaseUserManager):
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            token = Token.objects.create(user=instance)
            print(token)

    # def create_user(self, CustomID, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     return self._create_user(CustomID, password, **extra_fields)
    #
    # def create_superuser(self, CustomID, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     return self._create_user(CustomID, password, **extra_fields)
    #
    # def _create_user(self, CustomID, password, **extra_fields):
    #     user = self.model(
    #         CustomID=CustomID,
    #         **extra_fields
    #     )
    #
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_user(self, CustomID, password=None):
        user = self.model(
            CustomID=CustomID,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, CustomID, password):
        user = self.model(
            CustomID=CustomID,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(PermissionsMixin, AbstractBaseUser):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, null=True, blank=True, max_length=10)
    email = models.EmailField(max_length=50, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    CustomID = models.CharField(max_length=15, null=True, blank=True, unique=True)

    is_staff = models.BooleanField(default=False, blank=True)

    USERNAME_FIELD = 'CustomID'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

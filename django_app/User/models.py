from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from config import settings

GENDER_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUserManager(BaseUserManager):
    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_auth_token(sender, instance=None, created=False, **kwargs):
    #     if created:
    #         token = Token.objects.create(user=instance)
    #         print(token)

    def create_user(self, username, password=None, **extra_fields):
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(
            username=username,
            **extra_fields
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
    username = models.CharField(max_length=50, null=True, blank=True, unique=True, )
    is_staff = models.BooleanField(default=False, blank=True)
    profile_img = models.ImageField(upload_to='user', blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name



from django.db import models

from User.models import CustomUser


class Shop(models.Model):
    owner = models.ForeignKey(CustomUser, blank=True)
    shopname = models.CharField(max_length=30, blank=False)

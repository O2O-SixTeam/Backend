from django.conf import settings
from django.db import models


class Shop(models.Model):
    shopname = models.CharField(max_length=30, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop', blank=False)

    address = models.CharField(max_length=50, blank=True, null=True)
    detail = models.CharField(max_length=50, blank=True, null=True)
    video = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    zone = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Shop, self).save(*args, **kwargs)


# detail = models.CharField(max_length=100, blank=True, null=True),
#


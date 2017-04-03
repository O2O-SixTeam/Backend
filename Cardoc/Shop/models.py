from django.conf import settings
from django.db import models


class Shop(models.Model):
    shopname = models.CharField(max_length=30, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop', blank=False)

    def save(self, *args, **kwargs):
        super(Shop, self).save(*args, **kwargs)

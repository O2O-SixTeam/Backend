from django.conf import settings
from django.db import models

from Request.models import Request
from Shop.models import Shop


class Estimate(models.Model):
    #providedby = models.ForeignKey(Shop)
    #providedby = models.ForeignKey(Shop, related_name='shop', blank=False)
    #targetrequest = models.ForeignKey(Request, related_name='request', blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='estimate', blank=False)
    targetrequest = models.ForeignKey(Request)


    noninsurancecost = models.CharField(max_length=20, null=True, blank=True)
    insurancecost = models.CharField(max_length=20, null=True, blank=True)
    detail = models.CharField(max_length=200, null=True, blank=True)
    completed = models.NullBooleanField(blank=True, null=True)


    # def save(self, *args, **kwargs):
    #     super(Shop, self).save(*args, **kwargs)


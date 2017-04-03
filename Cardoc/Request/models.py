from django.conf import settings
from django.db import models

EXTRA_CHOICE = (
    ('보험수리', '보험수리'),
    ('렌터카', '렌터카'),
    ('픽업 서비스', '픽업 서비스'),
    ('차대번호', '차대번호'),
)


class Request(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request', blank=False)

    brand = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    carnumber = models.CharField(max_length=20, blank=True, null=True)
    broken1 = models.CharField(max_length=10, blank=True, null=True)
    broken2 = models.CharField(max_length=10, blank=True, null=True)
    broken3 = models.CharField(max_length=10, blank=True, null=True)
    photo1 = models.ImageField(max_length=None, blank=True, null=True)
    photo2 = models.ImageField(max_length=None, blank=True, null=True)
    photo3 = models.ImageField(max_length=None, blank=True, null=True)
    detail = models.CharField(max_length=200, blank=True, null=True)
    extra = models.CharField(choices=EXTRA_CHOICE, max_length=10, blank=True, null=True)
    number = models.CharField(max_length=11, blank=True, null=True)
    completed = models.NullBooleanField(blank=True,null=True)

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)

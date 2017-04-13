from django.conf import settings
from django.db import models

EXTRA_CHOICE = (
    ('보험수리', '보험수리'),
    ('렌터카', '렌터카'),
    ('픽업 서비스', '픽업 서비스'),
    ('차대번호', '차대번호'),
)

BROKEN_CHOICE = (
    ('범퍼', '범퍼'),
<<<<<<< HEAD
    ('프론트 판넬', '프론트 판넬'),
    ('앞 펜더', '앞 펜더'),
    ('앞 휠하우스', '앞 휠하우스'),
    ('에이필러', '에이필러'),
    ('앞문', '앞문'),
    ('비필러', '비필러'),
    ('뒷문', '뒷문'),
    ('뒤 펜더', '뒤 펜더'),
    ('뒤 휠하우스', '뒤 휠하우스'),
    ('루프판넬', '루프판넬'),
    ('트렁크', '트렁크'),
    ('리어 판넬', '리어 판넬'),
    ('본네트', '본네트'),
    ('유리', '유리'),
=======
    ('도어', '도어'),
    ('유리', '유리'),
    ('A 필러', 'A 필러'),
    ('B 필러', 'B 필러'),
    ('C 필러', 'C 필러'),
    ('본넷', '본넷'),
    ('루프 판넬', '루프 판넬'),
    ('트렁크', '트렁크'),
    ('휠하우스', '휠하우스'),
>>>>>>> master
)


class Request(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request', blank=False)

    brand = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    carnumber = models.CharField(max_length=20, blank=True, null=True)
    broken1 = models.CharField(choices=BROKEN_CHOICE, max_length=10, blank=True, null=True)
    broken2 = models.CharField(choices=BROKEN_CHOICE, max_length=10, blank=True, null=True)
    broken3 = models.CharField(choices=BROKEN_CHOICE, max_length=10, blank=True, null=True)
    photo1 = models.ImageField(max_length=None, blank=True, null=True)
    photo2 = models.ImageField(max_length=None, blank=True, null=True)
    photo3 = models.ImageField(max_length=None, blank=True, null=True)
    detail = models.CharField(max_length=200, blank=True, null=True)
    extra = models.CharField(choices=EXTRA_CHOICE, max_length=10, blank=True, null=True)
    number = models.CharField(max_length=11, blank=True, null=True)
    completed = models.NullBooleanField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)

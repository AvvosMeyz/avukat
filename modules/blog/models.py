from django.db import models
from django.conf import settings
from django.utils import timezone


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('başlık', max_length=200)
    text = models.TextField('yazı')
    created_date = models.DateTimeField('yazılan tarih',default=timezone.now)
    published_date = models.DateTimeField('paylaşılan tarih',blank=True, null=True)
    tag = models.CharField('etiket', max_length=50)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

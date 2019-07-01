from django.db import models
from django.conf import settings
from django.utils import timezone
import itertools
from slugify import slugify


class Category(models.Model):
    name = models.CharField('kategori', max_length=50)
    title = models.CharField('başlık', max_length=150)
    content = models.TextField('icerik')
    slug = models.SlugField(max_length=75, editable=False)
    image = models.ImageField(
        blank=True,
        null=True,
        default="static/img/default_blog.jpg", upload_to="static/img/%Y/%m/%d"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/img/default_blog.jpg"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField('başlık', max_length=200)
    text = models.TextField('yazı')
    created_date = models.DateTimeField('yazılan tarih',default=timezone.now)
    published_date = models.DateTimeField('paylaşılan tarih', blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False, max_length=100)
    image = models.ImageField(
        blank=True,
        null=True,
        default="static/img/default_blog.jpg", upload_to="static/img/%Y/%m/%d"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        max_length = BlogPost._meta.get_field('slug').max_length
        for x in itertools.count(1):
            if not BlogPost.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%s' % (self.slug[:max_length - len(str(x)) - 1], x)

        super(BlogPost, self).save()

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/img/default_blog.jpg"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Makale'
        verbose_name_plural = 'Makaleler'




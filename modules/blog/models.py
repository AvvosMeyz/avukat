from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify



kategoriler = [('1', 'Tazminat Hukuku'),
               ('2', 'Ceza Hukuku'),
               ('3', 'Medeni Hukuk'),
               ('4', 'Gayrimenkul Hukuku'),
               ('5', 'Vergi ve İdare Hukuku'),
               ('6', 'Bireysel Başvuru'),
               ('7', 'Arabulucuk'),
               ('8', 'Hukuk Haberleri'),
            ]


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('başlık', max_length=200)
    text = models.TextField('yazı')
    created_date = models.DateTimeField('yazılan tarih',default=timezone.now)
    published_date = models.DateTimeField('paylaşılan tarih', blank=True, null=True)
    tag = models.CharField('kategori', choices=kategoriler, max_length=50)
    slug = models.SlugField(max_length=150, default="gezegen_gezegen", unique=True)
    image = models.ImageField(
        blank=True,
        null=True,
        default="static/img/default_blog.jpg", upload_to="static/img/%Y/%m/%d"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/img/default_blog.jpg"

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'tag')


admin.site.register(BlogPost, BlogAdmin)

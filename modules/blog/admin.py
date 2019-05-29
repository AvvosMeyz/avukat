from django.contrib import admin
from .models import BlogPost
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(BlogPost, BlogAdmin)

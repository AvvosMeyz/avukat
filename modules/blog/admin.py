from django.contrib import admin
from .models import BlogPost, Category
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'created_date', 'image')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(BlogPost, BlogAdmin,)
admin.site.register(Category, CategoryAdmin,)

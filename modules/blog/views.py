from django.shortcuts import render
from .models import BlogPost


def index(request):
    latest_blog = BlogPost.objects.all()
    context = {
        'latest_blog': latest_blog,
    }
    return render(request, 'blog/blog-single.html', context)

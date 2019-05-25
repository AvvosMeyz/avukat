from django.shortcuts import render
from modules.blog.models import BlogPost


def index(request):
    latest_blog = BlogPost.objects.all()
    context = {
        'latest_blog': latest_blog,
    }
    return render(request, 'index/index.html', context)


def home(request):
    return render(request, 'blog/blog-single.html')

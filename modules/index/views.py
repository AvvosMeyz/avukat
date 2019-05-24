from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')


def home(request):
    return render(request, 'blog/blog-single.html')

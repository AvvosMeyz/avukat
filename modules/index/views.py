from django.shortcuts import render
from modules.blog.models import BlogPost


def index(request):
    last_three_items = BlogPost.objects.all().order_by('-id')[:3]
    last_item = last_three_items[0]
    mid_item = last_three_items[1]
    first_item = last_three_items[2]
    latest_blog = BlogPost.objects.all()
    context = {
        'latest_blog': latest_blog,
        'last_item': last_item,
        'mid_item': mid_item,
        'first_item': first_item,
        'last_three_items': last_three_items,
    }
    return render(request, 'index/index.html', context)


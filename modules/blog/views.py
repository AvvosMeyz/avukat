from django.shortcuts import render
from .models import BlogPost
from django.http import Http404
from django.db.models import Count


def index(request):
    latest_blog = BlogPost.objects.all()
    context = {
        'latest_blog': latest_blog,
    }
    return render(request, 'blog/index1.html', context)


def detail(request, id):
    try:
        blogpost = BlogPost.objects.get(pk=id)
        distinct_tags = BlogPost.objects.all().distinct('tag').order_by('tag')
        #Transaction.objects.all().values('actor').annotate(total=Count('actor')).order_by('total')
        distinct_tag_number = BlogPost.objects.all().values('tag').annotate(Count('id')).order_by('tag')
    except blogpost.DoesNotExist:
        raise Http404("Blog does not exist")
    context = {
        'distinct_tags': distinct_tags,
        'blogpost': blogpost,
        'distinct_tag_number': distinct_tag_number
    }

    return render(request, 'blog/blog-single.html', context)

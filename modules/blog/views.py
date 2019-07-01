from django.shortcuts import render
from .models import BlogPost, Category
from django.http import Http404
from django.db.models import Count
from django.shortcuts import render, get_object_or_404


def index(request):
    all_categories = Category.objects.all()
  #  latest_blog = BlogPost.objects.all()
 #   distinct_tags = BlogPost.objects.all().distinct('tag').order_by('tag')
 #   distinct_tag_number = BlogPost.objects.all().values('tag').annotate(Count('id')).order_by('tag')
    context = {
        'all_categories': all_categories,
  #      'distinct_tags': distinct_tags,
  #      'distinct_tag_number': distinct_tag_number,
    }
    return render(request, 'blog/category_select.html', context)


def detail(request, slug, slug2):
    blogpost = get_object_or_404(BlogPost, slug=slug2)

#   blogpost = BlogPost.objects.get(slug=slug)
  #  distinct_tags = BlogPost.objects.all().distinct('tag').order_by('tag')
#   Transaction.objects.all().values('actor').annotate(total=Count('actor')).order_by('total')
 #   distinct_tag_number = BlogPost.objects.all().values('tag').annotate(Count('id')).order_by('tag')
    context = {
 #       'distinct_tags': distinct_tags,
        'blogpost': blogpost,
 #       'distinct_tag_number': distinct_tag_number
    }
    return render(request, 'blog/blog-single.html', context)


def category_specific(request, slug):

    kategoriler = Category.objects.filter(slug=slug)

    cat = kategoriler.first()

    if cat.name == 'Ceza Hukuku':
        post = BlogPost.objects.filter(category__name='Ceza Hukuku')
    elif cat.name == 'Tazminat Hukuku':
        post = BlogPost.objects.filter(category__name='Tazminat Hukuku')
    elif cat.name == 'Medeni Hukuk':
        post = BlogPost.objects.filter(category__name='Medeni Hukuk')
    elif cat.name == 'Gayrimenkul Hukuku':
        post = BlogPost.objects.filter(category__name='Gayrimenkul Hukuku')
    elif cat.name == 'Vergi ve İdare Hukuku':
        post = BlogPost.objects.filter(category__name='Vergi ve İdare Hukuku Hukuku')
    elif cat.name == 'Bireysel Başvuru':
        post = BlogPost.objects.filter(category__name='Bireysel Başvuru')
    elif cat.name == 'Arabuluculuk':
        post = BlogPost.objects.filter(category__name='Arabuluculuk')
    elif cat.name == 'Hukuk Haberleri':
        post = BlogPost.objects.filter(category__name='Hukuk Haberleri')
    else:
        post = BlogPost.objects.all()

    context = {
        'cat': cat,
        'kategoriler': kategoriler,
        'post': post
    }
    return render(request, 'blog/category_spec.html', context)

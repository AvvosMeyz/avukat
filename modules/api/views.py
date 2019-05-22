from django.shortcuts import render
from modules.api.serializer import PostSerializer
from rest_framework import generics
from modules.blog.models import BlogPost


class PostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer

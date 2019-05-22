from django.urls import path
from modules.api import views

urlpatterns = [
    path('', views.PostListCreate.as_view()),
]
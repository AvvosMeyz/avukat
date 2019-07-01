from django.urls import path
from modules.blog import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='blog'),
    path('<str:slug>/', views.category_specific, name='category'),
    path('<str:slug>/<str:slug2>/', views.detail, name='detail'),
]
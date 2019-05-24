from django.urls import path
from modules.blog import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='blog'),

]
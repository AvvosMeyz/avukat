from django.urls import path
from modules.index import views

app_name = "index"
urlpatterns = [
    path('', views.index, name='index'),
]
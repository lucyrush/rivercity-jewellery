from django.urls import path
from . import views

from blog.views import blog, blog_detail

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]

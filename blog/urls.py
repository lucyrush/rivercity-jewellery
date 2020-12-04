from django.urls import path
from . import views

from blog.views import blog, blog_detail, category

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.category, name='category'),
]

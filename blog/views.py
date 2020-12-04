from django.shortcuts import render
from . models import Category, Post
from . forms import CommentForm


def blog(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)

    form = CommentForm()

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'blog/blog-detail.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        'category': category
    }

    return render(request, 'blog/category.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'carecardioblog/blog.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    recent_posts = Post.objects.exclude(pk=pk).order_by('-created_at')[:5]
    categories = Category.objects.all()
    return render(request, 'home/blog_detail.html', {'post': post, 'recent_posts': recent_posts, 'categories': categories})

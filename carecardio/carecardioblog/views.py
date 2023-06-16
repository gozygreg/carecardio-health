from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'carecardioblog/blog.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'home/blog_detail.html', {'post': post, 'category': category})

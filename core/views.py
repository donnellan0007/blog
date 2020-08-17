from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from django.contrib.auth import authenticate, login
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    latest = Post.objects.all()[0]
    context = {
        'posts' : posts,
        'latest' : latest
    }
    return render(request,'core/index.html', context)

def posts(request):
    posts = Post.objects.all().order_by("-timestamp")
    context = {
        'posts': posts
    }
    return render(request, 'core/posts.html',context)

def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'core/post.html',{'post':post})

def email(request):
    return render(request, 'core/email.html')
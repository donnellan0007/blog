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

def email(request):
    return render(request, 'core/email.html')
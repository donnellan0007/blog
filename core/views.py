from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from django.contrib.auth import authenticate, login
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    latest = Post.objects[0]
    context = {
        'posts' : posts,
        'latest' : latest
    }
    return render(request,'core/index.html', context)

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = request.user
            new_user = authenticate(username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            login(request, new_user)
            return redirect('core:index')
    else:
        form = ProfileForm()
    return render(request,'core/register.html', {'form' : form})

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

def verify(request):
    return render(request, 'core/verify.html')

from django.core.mail import send_mail
from magazine.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = request.user
            new_user = authenticate(username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            html_message = render_to_string('core/email.html', {'user':request.user})
            plain_message = strip_tags(html_message)
            email = form.cleaned_data.get('email')
            subject = 'Hello there!'
            message = 'Thank you for signing up to the OSC School Magazine'
            recipient = email
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            send_mail(subject, plain_message, EMAIL_HOST_USER, [recipient], html_message=html_message, fail_silently=False)
            login(request, new_user)
            return redirect('core:verify')
    else:
        form = ProfileForm()
    return render(request,'core/register.html', {'form' : form})


from django.http import JsonResponse
from django.contrib.auth.models import User

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['message'] = 'Someone with that username already exists!'
    return JsonResponse(data)
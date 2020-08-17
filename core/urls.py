from django.contrib import admin
from django.urls import path
from .views import index, email, post_detail, posts, hot_takes, take_detail
from . import views

app_name = "core"

urlpatterns = [
    path('',views.index,name="index"),
    path('email/',views.email,name="email"),
    path('post/<slug>/',views.post_detail,name='post'),
    path('posts/',views.posts,name='posts'),
    path('takes/',views.hot_takes,name='takes'),
    path('take/<slug>/',views.take_detail,name='take'),
]
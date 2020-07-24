from django.contrib import admin
from django.urls import path
from .views import index, register
from . import views

app_name = "core"

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register")
]

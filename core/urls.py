from django.contrib import admin
from django.urls import path
from .views import index, register, verify, validate_username
from . import views

app_name = "core"

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('verify', views.verify, name='verify'),
    path('ajax/validate_username/',views.validate_username,name='validate_username'),
]

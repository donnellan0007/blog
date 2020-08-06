from django.contrib import admin
from django.urls import path
from .views import index, email
from . import views

app_name = "core"

urlpatterns = [
    path('',views.index,name="index"),
    path('email/',views.email,name="email"),
]
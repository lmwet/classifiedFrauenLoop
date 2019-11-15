from django.contrib import admin
from django.urls import path

from .views import emailView, successView

urlpatterns = [
    path('profile/<pk>/email/', emailView, name='email'),
    path('success/', successView, name='success'),
]
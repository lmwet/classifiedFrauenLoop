from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    context = {
        'profiles': User.objects.all()
    }
    return render(request, 'public_profiles/home.html', context)

def about(request):
    return render(request, 'public_profiles/about.html', {'title': 'About'})
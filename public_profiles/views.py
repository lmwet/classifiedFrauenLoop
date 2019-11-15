from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from private_profiles.models import Profile
from django.views.generic import ListView, DetailView

def home(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'public_profiles/home.html', context)

class ProfileListView(ListView):
    model = Profile
    template_name = 'public_profiles/home.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'public_profiles/profile_details.html'
    

def about(request):
    return render(request, 'public_profiles/about.html', {'title': 'About'})
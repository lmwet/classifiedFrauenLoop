from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

profiles = [                                    # dummy data for landing site
    {
        'Username': 'Superduck',
        'Skills': 'Python, Django, Flask',
        'Dislikes': 'meat, ignorance',
        'Availablity': 'Starting from January 2020'
    },
    {
        'Username': 'Wonderspider',
        'Skills': 'Javascript, Bootstrap, HTML',
        'Dislikes': 'Antisemitism',
        'Availablity': 'Starting from February 2020'
    }
]

def home(request):
    context = {
        'profiles': User.objects.all()
    }
    return render(request, 'public_profiles/home.html', context)

def about(request):
    return render(request, 'public_profiles/about.html', {'title': 'About'})
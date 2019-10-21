from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ClassifiedRegistrationForm

def register(request):
    if request.method == 'POST':    # http POST request
        form = ClassifiedRegistrationForm(request.POST)     # extended forms model
        if form.is_valid():     # if form is filled out correctly (pre installed feature by django)
            form.save()         # input is saved in db
            username = form.cleaned_data.get('username')    # the username is retreived to be used in following step/ success message
            messages.success(request, f'You are now part of Classified Ads {username}! Please log in here!')
            return redirect('login')    # return to login route after registration is completed
    else:
        form = ClassifiedRegistrationForm()     # if form is not filled out correctly form is rendered again
    return render(request, 'private_profiles/register.html', {'form': form}) # in the register route with feedback

@login_required     # user needs to be logged in in order to accedd her profile site
def profiles_developer(request):
    return render(request, 'private_profiles/profiles_developer.html') 
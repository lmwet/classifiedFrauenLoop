from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from private_profiles.models import Profile
from django.views.generic import ListView, DetailView
from .forms import ContactForm



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

def emailView(request, pk):
    if request.method == 'GET':
        c_form = ContactForm()
    else:
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                m_send = EmailMessage(subject, message, from_email, ['admin@example.com'], cc=['riekeland@gmail.com'], bcc=['riekeland@compnay.com'])
                m_send.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "public_profiles/profile_details.html")

    # added context to make sure the correct form was being used - not sure if this is necessary
    context = {
        'c_form' : c_form,
    }

def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    # here we could also render a success template
    return render(request, 'public_profiles/success.html') 
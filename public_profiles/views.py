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

    def get(self, request, pk):
        self.object = self.get_object()
        form = ContactForm()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, pk):
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                #print(" What is in pk variable: ", pk)
                m_send = EmailMessage(subject, message, from_email, [pk])
                m_send.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
        return render(request, "public_profiles/profile_details.html", {'form': form})

def about(request):
    return render(request, 'public_profiles/about.html', {'title': 'About'})

def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    # here we could also render a success template
    return render(request, 'public_profiles/success.html') 
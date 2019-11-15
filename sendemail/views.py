from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                m_send = EmailMessage(subject, message, from_email, ['admin@example.com'], cc=['riekeland@gmail.com'], bcc=['riekeland@compnay.com'])
                m_send.send()
                #send_mail(subject, message, from_email, ['admin@example.com'], bcc=['riekeland@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "sendemail/email.html", {'form': form})

def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    # here we could also render a success template
    return render(request, 'sendemail/success.html') 
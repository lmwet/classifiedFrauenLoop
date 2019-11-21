from django import forms
from django.contrib.auth.models import User
from private_profiles.models import Profile

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
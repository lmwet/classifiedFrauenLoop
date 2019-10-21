from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClassifiedRegistrationForm(UserCreationForm):
    username = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Username'}))  # creating fields in addition to in-built User fields 
    email = forms.EmailField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))     # all fields habe a placeholder, label (above field) remains empty
    skills = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Skills'}))
    experience = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Experience'}))
    dislikes = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'What I dislike'}))
    availability = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Availability'}))
    password1 = forms.CharField(label='', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Enter the same password again'}))

    class Meta:
        model = User # our model is based on django's User model
        fields = ['username', 'email', 'skills', 'experience', 'dislikes', 'availability', 'password1', 'password2'] # succession of fields in order of appearance on site